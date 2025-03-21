"""
Video utilities for generating and combining Manim animations.
"""

import os
import subprocess
import tempfile
from pathlib import Path
import json
import re
from typing import List, Dict, Any, Optional
import shutil

from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

from src.core.animation_planner import Scene
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)


async def run_manim_scene(scene: Scene, output_dir: Path, ai_manager=None, max_retries: int = None) -> str:
    """
    Runs Manim code for a scene and returns the path to the generated video.
    
    Args:
        scene: Scene object with Manim code
        output_dir: Directory to save the video
        ai_manager: Optional AI manager for fixing code if it fails to run
        max_retries: Maximum number of retries when code fails (None for unlimited)
        
    Returns:
        Path to the generated video file
    """
    logger.info(f"Running Manim for scene: {scene.id}")
    
    # Skip if no Manim code is provided
    if not scene.manim_code:
        logger.warning(f"No Manim code provided for scene {scene.id}, using simple placeholder")
        return generate_placeholder_video(scene, output_dir)
    
    # Create a temporary Python file with the scene code
    scene_file = output_dir / f"{scene.id}.py"
    
    # Extract class name from the original manim code
    class_name = None
    if scene.manim_code:
        class_match = re.search(r"class\s+(\w+)\((Voice\w*Scene|Scene)\)", scene.manim_code)
        if class_match:
            class_name = class_match.group(1)
    
    # If no class name found, create a default one
    if not class_name:
        class_name = f"{scene.id.capitalize()}Scene"
        # Modify the code to use this class name
        modified_code = scene.manim_code.replace("class Scene(Scene):", f"class {class_name}(Scene):")
        if modified_code == scene.manim_code:  # If no replacement was made
            # Prepend class definition
            scene_code = f"from manim import *\n\nclass {class_name}(Scene):\n"
            # Indent the existing code if it doesn't already have a class definition
            if "class" not in scene.manim_code:
                scene_code += "\n".join(f"    {line}" for line in scene.manim_code.split("\n"))
            else:
                scene_code = scene.manim_code
        else:
            scene_code = modified_code
    else:
        scene_code = scene.manim_code
    
    # Write the scene code to the file
    with open(scene_file, "w") as f:
        f.write(scene_code)
    
    # Track the number of attempts
    attempts = 0
    current_code = scene_code
    
    # Attempt to run the code, with potential fixes from AI
    while max_retries is None or attempts <= max_retries:
        attempts += 1
        
        try:
            # Run manim with the scene class
            cmd = [
                "python", "-m", "manim",
                "-pqh",  # Preview quality high
                str(scene_file),
                class_name,
                f"--media_dir={output_dir}"
            ]
            
            logger.info(f"Running command: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Try to find the video in various locations where Manim might have saved it
            # Check in videos/<scene_id>/1080p60/
            possible_paths = [
                output_dir / "videos" / scene.id / "1080p60" / f"{class_name}.mp4",
                output_dir / "videos" / f"{scene.id}" / f"{class_name}.mp4",
                output_dir / "videos" / f"{class_name}.mp4",
                output_dir / "media" / "videos" / scene.id / "1080p60" / f"{class_name}.mp4",
                output_dir / "media" / "videos" / f"{scene.id}" / f"{class_name}.mp4",
                output_dir / "media" / "videos" / f"{class_name}.mp4"
            ]
            
            for path in possible_paths:
                if path.exists():
                    logger.info(f"Found video file: {path}")
                    
                    # Copy video to a standard location for easier syncing later
                    output_video = output_dir / f"{scene.id}_video.mp4"
                    shutil.copy(path, output_video)
                    logger.info(f"Copied video to {output_video}")
                    
                    return str(output_video)
            
            logger.error(f"Could not find generated video for scene: {scene.id}")
            logger.error(f"Manim output: {result.stdout}")
            
            # If no video was found but the command didn't error, try AI fix if available
            if ai_manager and (max_retries is None or attempts <= max_retries):
                logger.info(f"Attempting AI fix for scene {scene.id} (attempt {attempts})")
                
                # Debug logging for context validation
                has_narration = bool(scene.narration and scene.narration != "Error generating narration. Please try again.")
                has_animation_plan = bool(scene.animation_plan and scene.animation_plan.get('elements'))
                logger.debug(f"Scene {scene.id} context check - Narration: {has_narration}, Animation Plan: {has_animation_plan}")
                
                fixed_code = await ai_manager.fix_manim_code(
                    scene_id=scene.id,
                    scene_title=scene.title,
                    original_code=current_code,
                    error_output=f"Command succeeded but no video was produced:\n{result.stdout}",
                    narration=scene.narration,
                    animation_plan=scene.animation_plan,
                    output_dir=output_dir
                )
                
                if fixed_code:
                    logger.info(f"AI provided a fix for scene {scene.id}, retrying")
                    current_code = fixed_code
                    with open(scene_file, "w") as f:
                        f.write(fixed_code)
                    continue
            
            # If no AI manager or AI couldn't fix, return placeholder
            return generate_placeholder_video(scene, output_dir)
                
        except subprocess.CalledProcessError as e:
            logger.error(f"Error running Manim for scene {scene.id}: {e}")
            logger.error(f"STDOUT: {e.stdout}")
            logger.error(f"STDERR: {e.stderr}")
            
            # Try to fix with AI if available
            if ai_manager and (max_retries is None or attempts <= max_retries):
                logger.info(f"Attempting AI fix for scene {scene.id} (attempt {attempts})")
                
                # Debug logging for context validation
                has_narration = bool(scene.narration and scene.narration != "Error generating narration. Please try again.")
                has_animation_plan = bool(scene.animation_plan and scene.animation_plan.get('elements'))
                logger.debug(f"Scene {scene.id} context check - Narration: {has_narration}, Animation Plan: {has_animation_plan}")
                
                fixed_code = await ai_manager.fix_manim_code(
                    scene_id=scene.id,
                    scene_title=scene.title,
                    original_code=current_code,
                    error_output=f"STDOUT:\n{e.stdout}\n\nSTDERR:\n{e.stderr}",
                    narration=scene.narration,
                    animation_plan=scene.animation_plan,
                    output_dir=output_dir
                )
                
                if fixed_code:
                    logger.info(f"AI provided a fix for scene {scene.id}, retrying")
                    current_code = fixed_code
                    with open(scene_file, "w") as f:
                        f.write(fixed_code)
                    continue
            
            # If no AI manager or AI couldn't fix, return placeholder
            return generate_placeholder_video(scene, output_dir)
    
    # If we've exhausted all retries, use a placeholder
    logger.warning(f"Maximum retry attempts ({max_retries}) reached for scene {scene.id}, using placeholder")
    return generate_placeholder_video(scene, output_dir)


def generate_placeholder_video(scene: Scene, output_dir: Path) -> str:
    """
    Generates a simple placeholder video for a scene when Manim code fails to run.
    
    Args:
        scene: Scene object
        output_dir: Directory to save the video
        
    Returns:
        Path to the generated video file
    """
    scene_id = scene.id
    scene_title = scene.title
    
    # Create a temporary Python file with simple scene code
    scene_file = output_dir / f"{scene_id}_placeholder.py"
    class_name = f"{scene_id.capitalize()}PlaceholderScene"
    
    # Create a simple Manim scene that just displays a text
    simple_code = f"""
from manim import *

class {class_name}(Scene):
    def construct(self):
        # Create a text with the scene title/summary
        title = Text("{scene_title}", font_size=40)
        self.play(Write(title))
        self.wait(2)
        
        # Display a message indicating this is a placeholder
        subtitle = Text("Scene content replaced with simple animation", font_size=30, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle))
        self.wait(3)
        
        # Fade out everything
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(1)
"""
    
    # Write the simple scene code to the file
    with open(scene_file, "w") as f:
        f.write(simple_code)
    
    # Run Manim command to generate the video
    try:
        cmd = [
            "python", "-m", "manim",
            "-pqh",  # Preview quality high
            str(scene_file),
            class_name,
            f"--media_dir={output_dir}"
        ]
        
        logger.info(f"Running placeholder command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Try to find the video in various locations
        possible_paths = [
            output_dir / "videos" / f"{scene_id}_placeholder" / "1080p60" / f"{class_name}.mp4",
            output_dir / "videos" / f"{scene_id}_placeholder" / f"{class_name}.mp4",
            output_dir / "videos" / f"{class_name}.mp4",
            output_dir / "media" / "videos" / f"{scene_id}_placeholder" / "1080p60" / f"{class_name}.mp4",
            output_dir / "media" / "videos" / f"{scene_id}_placeholder" / f"{class_name}.mp4",
            output_dir / "media" / "videos" / f"{class_name}.mp4"
        ]
        
        for path in possible_paths:
            if path.exists():
                output_video = output_dir / f"{scene_id}_video.mp4"
                shutil.copy(path, output_video)
                return str(output_video)
        
        logger.error(f"Could not find generated placeholder video for scene: {scene_id}")
        return None
        
    except Exception as e:
        logger.error(f"Error generating placeholder video: {e}")
        return None


def get_media_duration(file_path: str) -> float:
    """
    Get the duration of a media file in seconds.
    
    Args:
        file_path: Path to the media file
        
    Returns:
        Duration in seconds
    """
    try:
        if file_path.endswith(".mp4") or file_path.endswith(".mov"):
            with VideoFileClip(file_path) as clip:
                return clip.duration
        elif file_path.endswith(".mp3") or file_path.endswith(".wav"):
            with AudioFileClip(file_path) as clip:
                return clip.duration
        else:
            logger.warning(f"Unsupported file format: {file_path}")
            return 0
    except Exception as e:
        logger.error(f"Error getting duration of {file_path}: {e}")
        return 0


def sync_video_with_audio(video_file: str, audio_file: str, output_file: str) -> str:
    """
    Sync a video with audio, ensuring the video lasts as long as the audio.
    If the video is shorter, the last frame will be extended.
    If the video is longer, it will be cut to match the audio duration.
    
    Args:
        video_file: Path to the video file
        audio_file: Path to the audio file
        output_file: Path to save the synced video
        
    Returns:
        Path to the synced video file
    """
    logger.info(f"Syncing video {video_file} with audio {audio_file}")
    
    try:
        with VideoFileClip(video_file) as video, AudioFileClip(audio_file) as audio:
            video_duration = video.duration
            audio_duration = audio.duration
            
            # If audio is longer, extend the video by freezing the last frame
            if audio_duration > video_duration:
                logger.info(f"Audio ({audio_duration}s) is longer than video ({video_duration}s). Extending video.")
                extended_video = video.fx(lambda clip: clip.set_duration(audio_duration))
                final_video = extended_video.set_audio(audio)
            else:
                # If video is longer, cut it to match audio duration
                logger.info(f"Video ({video_duration}s) is longer than audio ({audio_duration}s). Trimming video.")
                trimmed_video = video.subclip(0, audio_duration)
                final_video = trimmed_video.set_audio(audio)
            
            # Write the final video
            final_video.write_videofile(output_file, codec="libx264", audio_codec="aac")
            
            return output_file
    except Exception as e:
        logger.error(f"Error syncing video with audio: {e}")
        return None


def stitch_videos(video_files: List[str], output_file: str) -> str:
    """
    Stitch multiple videos together into a single video.
    
    Args:
        video_files: List of video file paths
        output_file: Path to save the stitched video
        
    Returns:
        Path to the stitched video file
    """
    logger.info(f"Stitching {len(video_files)} videos together")
    
    try:
        clips = [VideoFileClip(video) for video in video_files]
        final_clip = concatenate_videoclips(clips)
        
        # Write the final video
        final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        
        # Close all clips
        for clip in clips:
            clip.close()
        final_clip.close()
        
        logger.info(f"Stitched video saved to: {output_file}")
        return output_file
    except Exception as e:
        logger.error(f"Error stitching videos: {e}")
        return None


async def process_scene_videos(scenes: List[Scene], output_dir: Path, ai_manager=None, max_retries: int = None) -> List[Scene]:
    """
    Process all scenes by running Manim code and syncing videos with audio.
    
    Args:
        scenes: List of Scene objects
        output_dir: Directory to save processed videos
        ai_manager: Optional AI manager for fixing code if it fails to run
        max_retries: Maximum number of retries when code fails (None for unlimited)
        
    Returns:
        Updated list of Scene objects with video_file paths
    """
    updated_scenes = []
    
    for scene in scenes:
        logger.info(f"Processing video for scene: {scene.id}")
        
        # Skip scenes without audio
        if not scene.audio_file:
            logger.warning(f"Scene {scene.id} has no audio file, skipping video processing")
            updated_scenes.append(scene)
            continue
            
        # Create scene directory
        scene_dir = output_dir / scene.id
        scene_dir.mkdir(exist_ok=True, parents=True)
        
        # Check if synced video already exists
        synced_video_file = str(scene_dir / f"{scene.id}_synced.mp4")
        if scene.video_file and os.path.exists(scene.video_file):
            logger.info(f"Video file already exists for scene {scene.id}, reusing: {scene.video_file}")
            updated_scenes.append(scene)
            continue
        elif os.path.exists(synced_video_file):
            logger.info(f"Synced video file already exists for scene {scene.id}, reusing: {synced_video_file}")
            updated_scene = Scene(
                id=scene.id,
                title=scene.title,
                duration=scene.duration,
                narration=scene.narration,
                animation_plan=scene.animation_plan,
                original_query=scene.original_query,
                original_solution=scene.original_solution,
                manim_code=scene.manim_code,
                audio_file=scene.audio_file,
                video_file=synced_video_file
            )
            updated_scenes.append(updated_scene)
            continue
            
        # Generate video from Manim
        video_file = await run_manim_scene(scene, scene_dir, ai_manager, max_retries)
        
        if not video_file:
            logger.error(f"Failed to generate video for scene {scene.id}")
            updated_scenes.append(scene)
            continue
            
        # Sync video with audio
        if scene.audio_file and os.path.exists(scene.audio_file):
            synced_video = sync_video_with_audio(
                video_file=video_file,
                audio_file=scene.audio_file,
                output_file=synced_video_file
            )
            
            if not synced_video:
                logger.error(f"Failed to sync video with audio for scene {scene.id}")
                updated_scene = Scene(
                    id=scene.id,
                    title=scene.title,
                    duration=scene.duration,
                    narration=scene.narration,
                    animation_plan=scene.animation_plan,
                    original_query=scene.original_query,
                    original_solution=scene.original_solution,
                    manim_code=scene.manim_code,
                    audio_file=scene.audio_file,
                    video_file=video_file  # Use the unsynced video
                )
            else:
                logger.info(f"Video synced with audio for scene {scene.id}")
                updated_scene = Scene(
                    id=scene.id,
                    title=scene.title,
                    duration=scene.duration,
                    narration=scene.narration,
                    animation_plan=scene.animation_plan,
                    original_query=scene.original_query,
                    original_solution=scene.original_solution,
                    manim_code=scene.manim_code,
                    audio_file=scene.audio_file,
                    video_file=synced_video
                )
        else:
            logger.warning(f"No audio file for scene {scene.id}, using video without audio")
            updated_scene = Scene(
                id=scene.id,
                title=scene.title,
                duration=scene.duration,
                narration=scene.narration,
                animation_plan=scene.animation_plan,
                original_query=scene.original_query,
                original_solution=scene.original_solution,
                manim_code=scene.manim_code,
                audio_file=None,
                video_file=video_file
            )
            
        updated_scenes.append(updated_scene)
        
    return updated_scenes


def create_final_video(scenes: List[Scene], output_file: str) -> str:
    """
    Create the final video by stitching all scene videos together.
    
    Args:
        scenes: List of Scene objects with video_file paths
        output_file: Path to save the final video
        
    Returns:
        Path to the final video file
    """
    # Check if final video already exists
    if os.path.exists(output_file):
        logger.info(f"Final video already exists, reusing: {output_file}")
        return output_file
        
    # Collect all scene videos that exist
    video_files = [scene.video_file for scene in scenes if scene.video_file and os.path.exists(scene.video_file)]
    
    if not video_files:
        logger.error("No valid video files found to stitch together")
        return None
        
    logger.info(f"Creating final video from {len(video_files)} scene videos")
    
    # Stitch videos together
    return stitch_videos(video_files, output_file) 


def clean_manim_code_file(file_path: str) -> Optional[str]:
    """
    Cleans a Manim code file that may contain explanatory text or non-code elements.
    
    Args:
        file_path: Path to the Manim code file
        
    Returns:
        Path to the cleaned file or None if cleaning failed
    """
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return None
        
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Check for <CODE> tags
        code_blocks = re.findall(r'<CODE>\n?(.*?)\n?</CODE>', content, re.DOTALL)
        if code_blocks:
            clean_code = code_blocks[0].strip()
        # Check for markdown-style code blocks
        elif "```python" in content and "```" in content:
            code_parts = content.split("```python")
            if len(code_parts) > 1:
                clean_code = code_parts[1].split("```")[0].strip()
            else:
                clean_code = content  # Fallback
        else:
            # Try to find where explanatory text starts
            lines = content.split('\n')
            code_lines = []
            in_explanatory_text = False
            
            for line in lines:
                # Skip initial comments that look like explanations
                if (not code_lines and 
                    (line.startswith("I'll create") or 
                     line.startswith("This animation") or
                     line.startswith("<CODE>"))):
                    continue
                    
                # Stop when we hit explanatory text
                if line.strip() == "" and len(code_lines) > 0:
                    next_index = lines.index(line) + 1 if line in lines and lines.index(line) < len(lines) - 1 else -1
                    if next_index > 0 and next_index < len(lines):
                        next_line = lines[next_index].strip()
                        if (next_line.startswith("This ") or 
                            next_line.startswith("The ") or 
                            next_line.startswith("</CODE>") or
                            re.match(r'^\d+\.', next_line)):
                            in_explanatory_text = True
                            break
                
                if not in_explanatory_text:
                    code_lines.append(line)
            
            clean_code = '\n'.join(code_lines).strip()
        
        # Write the cleaned code to a new file
        cleaned_file_path = file_path.replace('.py', '_cleaned.py')
        with open(cleaned_file_path, 'w') as f:
            f.write(clean_code)
            
        logger.info(f"Cleaned Manim code file saved to {cleaned_file_path}")
        return cleaned_file_path
        
    except Exception as e:
        logger.error(f"Error cleaning Manim code file: {e}")
        return None