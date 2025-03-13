"""
Media Processor Module for Manim Video Generator.

This module handles the rendering of Manim animations, voice synthesis,
and synchronization of audio and video components.
"""

import os
import json
import tempfile
import asyncio
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import ffmpeg
import re
import shutil

from pydantic import BaseModel, Field
from src.utils.kokoro_voiceover import KokoroService
from src.utils.logging_utils import get_logger
from src.config.config import Config

logger = get_logger(__name__)


class MediaSegment(BaseModel):
    """Data model for a media segment with synchronized audio and video."""
    section_id: str
    video_path: str
    audio_path: str
    script: str
    duration: float
    start_time: float = 0.0


class MediaProcessor:
    """
    Handles the rendering of Manim animations and synchronization with audio.
    """
    
    def __init__(self, output_dir: str = Config.OUTPUT_DIR):
        """
        Initialize the media processor.
        
        Args:
            output_dir: Directory for output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)
        
        # Initialize TTS service
        self.tts_service = KokoroService()
        
        # Create temporary directory for intermediate files
        self.temp_dir = Path(tempfile.mkdtemp())
        logger.info(f"Created temporary directory: {self.temp_dir}")
    
    async def generate_voiceover(self, section_id: str, script: str) -> str:
        """
        Generate voice audio for a script segment.
        
        Args:
            section_id: Section identifier
            script: Narration script text
            
        Returns:
            Path to the generated audio file
        """
        logger.info(f"Generating voiceover for section {section_id}")
        
        # Create an MP3 path in the temp directory
        audio_path = self.temp_dir / f"{section_id}_audio.mp3"
        
        # Generate the audio file using the TTS service
        try:
            result = self.tts_service.generate_from_text(
                text=script,
                cache_dir=str(self.temp_dir),
                path=str(audio_path.name)
            )
            
            # Get the full path to the generated file
            audio_path = self.temp_dir / result["original_audio"]
            logger.info(f"Voiceover generated successfully: {audio_path}")
            
            return str(audio_path)
        except Exception as e:
            logger.error(f"Failed to generate voiceover: {str(e)}")
            raise
    
    async def run_manim_render(self, code: str, output_name: str) -> str:
        """
        Run Manim to render the animation.
        
        Args:
            code: Manim Python code
            output_name: Base name for the output files
            
        Returns:
            Path to the rendered video file
        """
        logger.info(f"Starting Manim rendering for {output_name}")
        
        # Save the Manim code to a temporary Python file
        code_file = self.temp_dir / f"{output_name}.py"
        with open(code_file, "w") as f:
            f.write(code)
        
        # Run Manim with the -qm (medium quality) flag for faster rendering
        cmd = [
            "python3", "-m", "manim", 
            str(code_file),
            "MathAnimation",  # assuming the scene class is named MathAnimation
            "-qm",
            "--media_dir", str(self.temp_dir)
        ]
        
        # Execute the command and capture output
        try:
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode != 0:
                logger.error(f"Manim rendering failed: {stderr.decode()}")
                raise Exception(f"Manim rendering failed with code {process.returncode}")
            
            # Parse the output to find the rendered video file path
            output = stdout.decode()
            logger.debug(f"Manim output: {output}")
            
            # Video is usually in media/videos/{output_name}/MathAnimation.mp4
            video_dir = self.temp_dir / "media" / "videos" / output_name
            video_file = video_dir / "MathAnimation.mp4"
            
            if not video_file.exists():
                # Try to find the video file by glob pattern
                video_files = list(video_dir.glob("*.mp4"))
                if video_files:
                    video_file = video_files[0]
                else:
                    raise FileNotFoundError(f"Could not find rendered video file in {video_dir}")
            
            logger.info(f"Manim rendering completed: {video_file}")
            return str(video_file)
            
        except Exception as e:
            logger.error(f"Error running Manim: {str(e)}")
            raise
    
    async def synchronize_audio_video(
        self, 
        video_path: str, 
        audio_path: str, 
        output_path: str,
        extend_last_frame: bool = True
    ) -> str:
        """
        Synchronize audio with video, extending the last frame if audio is longer.
        
        Args:
            video_path: Path to the video file
            audio_path: Path to the audio file
            output_path: Path for the synchronized output
            extend_last_frame: Whether to extend the last frame if audio is longer
            
        Returns:
            Path to the synchronized video file
        """
        logger.info(f"Synchronizing audio and video: {os.path.basename(video_path)} + {os.path.basename(audio_path)}")
        
        try:
            # Get durations
            video_duration = float(ffmpeg.probe(video_path)["format"]["duration"])
            audio_duration = float(ffmpeg.probe(audio_path)["format"]["duration"])
            
            logger.info(f"Video duration: {video_duration}s, Audio duration: {audio_duration}s")
            
            if audio_duration > video_duration and extend_last_frame:
                logger.info(f"Audio is longer than video by {audio_duration - video_duration}s, extending last frame")
                
                # Extract the last frame
                last_frame_path = self.temp_dir / "last_frame.png"
                (
                    ffmpeg
                    .input(video_path, ss=video_duration-0.1)
                    .output(str(last_frame_path), vframes=1)
                    .run(quiet=True, overwrite_output=True)
                )
                
                # Create an extended video with the last frame held
                extended_video_path = self.temp_dir / "extended_video.mp4"
                extended_duration = audio_duration - video_duration
                
                # First, create a video of the last frame with the required duration
                (
                    ffmpeg
                    .input(str(last_frame_path), loop=1, t=extended_duration)
                    .output(str(self.temp_dir / "last_frame_video.mp4"), vcodec="libx264", pix_fmt="yuv420p")
                    .run(quiet=True, overwrite_output=True)
                )
                
                # Then concatenate the original video with the last frame video
                concat_file = self.temp_dir / "concat.txt"
                with open(concat_file, "w") as f:
                    f.write(f"file '{video_path}'\nfile '{self.temp_dir / 'last_frame_video.mp4'}'")
                
                (
                    ffmpeg
                    .input(str(concat_file), format="concat", safe=0)
                    .output(str(extended_video_path), c="copy")
                    .run(quiet=True, overwrite_output=True)
                )
                
                # Use the extended video for synchronization
                video_to_use = str(extended_video_path)
            else:
                video_to_use = video_path
            
            # Add audio to the video
            (
                ffmpeg
                .input(video_to_use)
                .input(audio_path)
                .output(
                    output_path, 
                    vcodec="copy", 
                    acodec="aac", 
                    strict="experimental", 
                    shortest=False
                )
                .run(quiet=True, overwrite_output=True)
            )
            
            logger.info(f"Synchronized media created: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error synchronizing audio and video: {str(e)}")
            raise
    
    async def process_section(
        self, 
        section_id: str,
        script: str,
        manim_code: str,
    ) -> MediaSegment:
        """
        Process a single section of the video.
        
        Args:
            section_id: Section identifier
            script: Narration script
            manim_code: Manim code for the section
            
        Returns:
            Media segment with synchronized audio and video
        """
        logger.info(f"Processing section: {section_id}")
        
        # Generate tasks for concurrent processing
        voice_task = asyncio.create_task(self.generate_voiceover(section_id, script))
        render_task = asyncio.create_task(self.run_manim_render(manim_code, section_id))
        
        # Wait for both tasks to complete
        audio_path, video_path = await asyncio.gather(voice_task, render_task)
        
        # Synchronize audio and video
        output_path = str(self.temp_dir / f"{section_id}_synchronized.mp4")
        synchronized_path = await self.synchronize_audio_video(video_path, audio_path, output_path)
        
        # Get the duration of the synchronized video
        duration = float(ffmpeg.probe(synchronized_path)["format"]["duration"])
        
        # Create and return the media segment
        segment = MediaSegment(
            section_id=section_id,
            video_path=synchronized_path,
            audio_path=audio_path,
            script=script,
            duration=duration
        )
        
        return segment
    
    async def combine_segments(self, segments: List[MediaSegment], output_name: str) -> str:
        """
        Combine multiple media segments into a final video.
        
        Args:
            segments: List of media segments to combine
            output_name: Name for the output file
            
        Returns:
            Path to the final video file
        """
        logger.info(f"Combining {len(segments)} segments into final video")
        
        # Sort segments by section_id
        sorted_segments = sorted(segments, key=lambda s: s.section_id)
        
        # Create a file listing all segments for concatenation
        concat_file = self.temp_dir / "concat_final.txt"
        with open(concat_file, "w") as f:
            for segment in sorted_segments:
                f.write(f"file '{segment.video_path}'\n")
        
        # Output path for the final video
        final_output = self.output_dir / f"{output_name}.mp4"
        
        # Combine all segments using FFmpeg
        (
            ffmpeg
            .input(str(concat_file), format="concat", safe=0)
            .output(str(final_output), c="copy")
            .run(quiet=True, overwrite_output=True)
        )
        
        logger.info(f"Final video created: {final_output}")
        return str(final_output)
    
    def cleanup(self):
        """Clean up temporary files."""
        logger.info(f"Cleaning up temporary directory: {self.temp_dir}")
        shutil.rmtree(self.temp_dir)


class VideoGenerator:
    """
    High-level interface for generating complete educational videos.
    """
    
    def __init__(self, output_dir: str = Config.OUTPUT_DIR):
        """
        Initialize the video generator.
        
        Args:
            output_dir: Directory for output files
        """
        self.media_processor = MediaProcessor(output_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)
    
    async def generate_video(
        self, 
        scripts: Dict[str, str],
        manim_code: str,
        title: str,
        metadata: Dict[str, Any] = None
    ) -> str:
        """
        Generate a complete video with synchronized audio and animations.
        
        Args:
            scripts: Dictionary mapping section IDs to narration scripts
            manim_code: Complete Manim code for all sections
            title: Video title
            metadata: Additional metadata to save with the video
            
        Returns:
            Path to the final video file
        """
        try:
            logger.info(f"Starting video generation for: {title}")
            
            # Process the sections concurrently
            sections = []
            tasks = []
            
            for section_id, script in scripts.items():
                # Each section needs its own Manim code
                # For now, we'll use the same code for all sections
                # In a more sophisticated implementation, we'd split the code by section
                task = self.media_processor.process_section(section_id, script, manim_code)
                tasks.append(task)
            
            # Wait for all section processing to complete
            segments = await asyncio.gather(*tasks)
            
            # Combine the segments into the final video
            safe_title = re.sub(r'[^\w\-_]', '_', title)
            final_video_path = await self.media_processor.combine_segments(segments, safe_title)
            
            # Save metadata
            if metadata:
                metadata_path = self.output_dir / f"{safe_title}_metadata.json"
                with open(metadata_path, "w") as f:
                    json.dump(metadata, f, indent=2)
            
            # Clean up temporary files
            self.media_processor.cleanup()
            
            logger.info(f"Video generation completed: {final_video_path}")
            return final_video_path
            
        except Exception as e:
            logger.error(f"Error generating video: {str(e)}")
            # Attempt cleanup even on failure
            self.media_processor.cleanup()
            raise 