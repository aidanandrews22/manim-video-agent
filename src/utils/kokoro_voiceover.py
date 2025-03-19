"""
Copyright (c) 2025 Xposed73
All rights reserved.
This file is part of the Manim Voiceover project.
"""

import hashlib
import json
import numpy as np
import os
from pathlib import Path
from manim_voiceover.services.base import SpeechService
from kokoro_onnx import Kokoro
from manim_voiceover.helper import remove_bookmarks, wav2mp3
from scipy.io.wavfile import write as write_wav
from src.config.config import Config
from src.core.animation_planner import Scene

from src.utils.logging_utils import get_logger

logger = get_logger(__name__)


class KokoroService(SpeechService):
    """Speech service class for kokoro_self (using text_to_speech via Kokoro ONNX)."""

    def __init__(self, engine=None, 
                 model_path: str = Config.KOKORO_MODEL_PATH,
                 voices_path: str = Config.KOKORO_VOICES_PATH,
                 voice: str = Config.KOKORO_DEFAULT_VOICE,
                 speed: float = Config.KOKORO_DEFAULT_SPEED,
                 lang: str = Config.KOKORO_DEFAULT_LANG,
                 **kwargs):
        self.kokoro = Kokoro(model_path, voices_path)
        self.voice = voice
        self.speed = speed
        self.lang = lang

        if engine is None:
            engine = self.text_to_speech  # Default to local function

        self.engine = engine
        super().__init__(**kwargs)

    def get_data_hash(self, input_data: dict) -> str:
        """
        Generates a hash based on the input data dictionary.
        The hash is used to create a unique identifier for the input data.

        Parameters:
            input_data (dict): A dictionary of input data (e.g., text, voice, etc.).

        Returns:
            str: The generated hash as a string.
        """
        # Convert the input data dictionary to a JSON string (sorted for consistency)
        data_str = json.dumps(input_data, sort_keys=True)
        # Generate a SHA-256 hash of the JSON string
        return hashlib.sha256(data_str.encode('utf-8')).hexdigest()

    def text_to_speech(self, text, output_file, voice_name, speed, lang):
        """
        Generates speech from text using Kokoro ONNX and saves the audio file.
        Normalizes the audio to make it audible.
        """
        # Generate audio samples using Kokoro
        samples, sample_rate = self.kokoro.create(
            text, voice=voice_name, speed=speed, lang=lang
        )

        # Normalize audio to the range [-1, 1]
        max_val = np.max(np.abs(samples))
        if max_val > 0:
            samples = samples / max_val

        # Convert to 16-bit integer PCM format
        samples = (samples * 32767).astype("int16")

        # Save the normalized audio as a .wav file
        write_wav(output_file, sample_rate, samples)
        logger.info(f"Audio saved at {output_file}")

        return output_file


    def generate_from_text(self, text: str, cache_dir: str = None, path: str = None) -> dict:
        if cache_dir is None:
            cache_dir = self.cache_dir

        # Convert cache_dir to Path object if it's a string
        cache_dir_path = Path(cache_dir) if isinstance(cache_dir, str) else cache_dir

        input_data = {"input_text": text, "service": "kokoro_self", "voice": self.voice, "lang": self.lang}
        cached_result = self.get_cached_result(input_data, cache_dir_path)
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_data_hash(input_data) + ".mp3"
        else:
            audio_path = path

        # Generate .wav file using the text_to_speech function
        audio_path_wav = str(Path(cache_dir) / audio_path.replace(".mp3", ".wav"))
        
        self.engine(
            text=text,
            output_file=audio_path_wav,
            voice_name=self.voice,
            speed=self.speed,
            lang=self.lang,
        )

        # Convert .wav to .mp3
        mp3_audio_path = str(Path(cache_dir) / audio_path)
        
        wav2mp3(audio_path_wav, mp3_audio_path)

        # Remove original .wav file
        remove_bookmarks(audio_path_wav)

        json_dict = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }

        return json_dict


def generate_scene_audio(scene: Scene, output_dir: Path) -> str:
    """
    Generate audio for a scene using Kokoro TTS.
    
    Args:
        scene: The scene object containing narration
        output_dir: Directory to save the audio file
        
    Returns:
        Path to the generated audio file
    """
    logger.info(f"Generating audio for scene: {scene.id}")
    
    # Define the audio file paths
    audio_filename = f"{scene.id}_audio.mp3"
    audio_path = str(output_dir / audio_filename)
    
    # Check if audio file already exists
    if os.path.exists(audio_path):
        logger.info(f"Audio file already exists for scene {scene.id}, reusing: {audio_path}")
        return audio_path
    
    # Create the Kokoro service
    service = KokoroService(
        cache_dir=str(output_dir)
    )
    
    # Generate audio file
    try:
        result = service.generate_from_text(
            text=scene.narration,
            path=audio_filename
        )
        
        # Update scene with audio file path
        audio_file = os.path.join(str(output_dir), result["original_audio"])
        logger.info(f"Audio generated for scene {scene.id}: {audio_file}")
        
        return audio_file
    except Exception as e:
        logger.error(f"Error generating audio for scene {scene.id}: {e}")
        import traceback
        traceback.print_exc()
        return None
        
        
async def generate_audio_for_scenes(scenes: list[Scene], output_dir: Path) -> list[Scene]:
    """
    Generate audio for all scenes in a video.
    
    Args:
        scenes: List of Scene objects
        output_dir: Directory to save audio files
        
    Returns:
        Updated list of Scene objects with audio_file paths
    """
    import asyncio
    from concurrent.futures import ThreadPoolExecutor
    
    updated_scenes = []
    
    # Create a thread pool for the synchronous audio generation
    with ThreadPoolExecutor(max_workers=4) as executor:
        loop = asyncio.get_running_loop()
        tasks = []
        
        for scene in scenes:
            # Check if scene already has an audio file
            if scene.audio_file and os.path.exists(scene.audio_file):
                logger.info(f"Scene {scene.id} already has an audio file, reusing: {scene.audio_file}")
                updated_scenes.append(scene)
                continue
                
            # Create directory for scene if it doesn't exist
            scene_dir = os.path.join(str(output_dir), scene.id)
            os.makedirs(scene_dir, exist_ok=True)
            
            # Run audio generation in thread pool
            task = loop.run_in_executor(
                executor,
                generate_scene_audio,
                scene,
                Path(scene_dir)
            )
            tasks.append((scene, task))
        
        # Wait for all tasks to complete
        for scene, task in tasks:
            audio_file = await task
            
            # Update scene with audio file path
            updated_scene = Scene(
                id=scene.id,
                title=scene.title,
                duration=scene.duration,
                narration=scene.narration,
                animation_plan=scene.animation_plan,
                original_query=scene.original_query,
                original_solution=scene.original_solution,
                manim_code=scene.manim_code,
                audio_file=audio_file,
                video_file=scene.video_file
            )
            
            updated_scenes.append(updated_scene)
            
    return updated_scenes