"""
Main entry point for the Manim Video Agent application.
"""

import argparse
import asyncio
import json
import os
from pathlib import Path
import sys

from src.config.config import Config
from src.core.ai_manager import AIManager
from src.core.animation_planner import AnimationPlan, Scene
from src.utils.kokoro_voiceover import generate_audio_for_scenes
from src.utils.video_utils import process_scene_videos, create_final_video
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)


async def generate_video(problem: str, output_dir: str, config: Config, use_cache: bool = True):
    """
    Generate a complete educational math video from a problem statement.
    
    Args:
        problem: The mathematical problem or concept to explain
        output_dir: Directory to save the generated files
        config: Configuration object
        use_cache: Whether to use caching for AI responses
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)
    
    # Initialize AI manager
    ai_manager = AIManager(config, use_cache=use_cache)
    
    # Step 1: Solve the math problem with o3-mini
    logger.info("Solving the math problem...")
    solution = await ai_manager.solve_or_explain(problem)
    
    with open(output_path / "solution.txt", "w") as f:
        f.write(solution)
    
    # Step 2: Create scene-based animation plan with o3-mini
    logger.info("Creating scene-based animation plan...")
    scene_plan = await ai_manager.create_scene_plan(problem, solution)
    
    with open(output_path / "scene_plan.json", "w") as f:
        json.dump(scene_plan, f, indent=2)
    
    # Step 3: Process each scene using Gemini and Claude
    scenes = []
    for scene_data in scene_plan.get("scenes", []):
        logger.info(f"Processing scene: {scene_data.get('id', 'unknown')}")
        
        scene = await ai_manager.process_scene(
            scene_data=scene_data,
            query=problem,
            explanation=solution,
            output_dir=output_path
        )
        
        scenes.append(scene)
    
    # Save the list of scenes
    scenes_data = [scene.model_dump() for scene in scenes]
    with open(output_path / "scenes.json", "w") as f:
        json.dump(scenes_data, f, indent=2)
    
    # Step 4 & 5: Generate audio and video for each scene in parallel
    logger.info("Generating audio and video code concurrently for all scenes...")
    
    # Use the async version for batch processing of all scenes
    scenes_with_audio = await generate_audio_for_scenes(scenes, output_path)
    
    # Step 6: Process videos with the audio
    logger.info("Processing videos for all scenes...")
    final_scenes = await process_scene_videos(
        scenes_with_audio, 
        output_path, 
        ai_manager=ai_manager,
        max_retries=None  # No limit on retries
    )
    
    # Step 7: Stitch all scene videos together
    logger.info("Creating final video...")
    final_video_path = str(output_path / "final_video.mp4")
    final_video = create_final_video(final_scenes, final_video_path)
    
    if final_video:
        logger.info(f"Video generation complete. Final video saved to {final_video}")
    else:
        logger.error("Failed to create final video")
    
    # Log usage statistics
    usage_stats = ai_manager.get_model_usage()
    logger.info(f"AI usage statistics: {usage_stats}")
    
    return final_video


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="Generate educational math videos using Manim")
    parser.add_argument("problem", help="The mathematical problem or concept to explain")
    parser.add_argument("--output", "-o", default="output", help="Directory to save the generated files")
    parser.add_argument("--no-cache", action="store_true", help="Disable caching of AI responses")
    args = parser.parse_args()
    
    # Load configuration
    config = Config()
    
    # Check for required API keys
    if not config.OPENAI_API_KEY:
        logger.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        sys.exit(1)
    
    if not config.ANTHROPIC_API_KEY:
        logger.error("Anthropic API key not found. Please set the ANTHROPIC_API_KEY environment variable.")
        sys.exit(1)
    
    if not config.GEMINI_API_KEY:
        logger.error("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")
        sys.exit(1)
    
    # Run the video generation process
    asyncio.run(generate_video(args.problem, args.output, config, use_cache=not args.no_cache))


if __name__ == "__main__":
    main() 