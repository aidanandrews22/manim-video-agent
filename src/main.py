"""
Main entry point for the Manim Video Agent application.
"""

import argparse
import asyncio
import json
import os
from pathlib import Path

from src.config.config import Config
from src.core.ai_manager import AIManager
from src.core.animation_planner import AnimationPlan
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
    
    # Step 1: Solve the math problem
    logger.info("Solving the math problem...")
    solution = await ai_manager.solve_math_problem(problem)
    
    with open(output_path / "solution.txt", "w") as f:
        f.write(solution)
    
    # Step 2: Create animation plan
    logger.info("Creating animation plan...")
    animation_plan = await ai_manager.create_animation_plan(
        problem,
        solution
    )
    
    with open(output_path / "animation_plan.json", "w") as f:
        f.write(animation_plan.model_dump_json(indent=2))
    
    # Step 3: Generate script
    logger.info("Generating script...")
    script = await ai_manager.generate_script(animation_plan)
    
    with open(output_path / "script.json", "w") as f:
        json.dump(script, f, indent=2)
    
    # Step 4: Generate Manim code
    logger.info("Generating Manim code...")
    manim_code = await ai_manager.generate_manim_code(animation_plan, script)
    
    with open(output_path / "animation.py", "w") as f:
        f.write(manim_code)
    
    # Step 5: Run the Manim code (optional)
    # This would require Manim to be installed and configured
    
    logger.info(f"Video generation complete. Files saved to {output_path}")
    
    # Log usage statistics
    usage_stats = ai_manager.get_model_usage()
    logger.info(f"AI usage statistics: {usage_stats}")


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="Generate educational math videos using Manim")
    parser.add_argument("problem", help="The mathematical problem or concept to explain")
    parser.add_argument("--output", "-o", default="output", help="Directory to save the generated files")
    parser.add_argument("--no-cache", action="store_true", help="Disable caching of AI responses")
    args = parser.parse_args()
    
    # Load configuration
    config = Config()
    
    # Run the video generation process
    asyncio.run(generate_video(args.problem, args.output, config, use_cache=not args.no_cache))


if __name__ == "__main__":
    main() 