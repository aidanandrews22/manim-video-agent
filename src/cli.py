#!/usr/bin/env python3
"""
Command-line interface for the Manim Video Generator.
"""

import os
import sys
import asyncio
import argparse
import json
from typing import Dict, Any, Optional
from pathlib import Path

from src.core.pipeline import generate_math_video
from src.config.config import Config
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate educational math videos with Manim."
    )
    
    parser.add_argument(
        "query",
        type=str,
        help="Mathematical topic or problem to explain"
    )
    
    parser.add_argument(
        "--category",
        type=str,
        choices=["theorem", "problem", "concept", "definition", "proof"],
        help="Category of mathematical content"
    )
    
    parser.add_argument(
        "--difficulty",
        type=str,
        choices=["elementary", "high school", "undergraduate", "graduate"],
        help="Target difficulty level"
    )
    
    parser.add_argument(
        "--max-duration",
        type=int,
        default=180,
        help="Maximum video duration in seconds (default: 180)"
    )
    
    parser.add_argument(
        "--focus",
        type=str,
        nargs="+",
        help="Specific areas to focus on in the explanation"
    )
    
    parser.add_argument(
        "--output-dir",
        type=str,
        default=Config.OUTPUT_DIR,
        help=f"Output directory (default: {Config.OUTPUT_DIR})"
    )
    
    parser.add_argument(
        "--openai-key",
        type=str,
        default=os.environ.get("OPENAI_API_KEY"),
        help="OpenAI API key (default: from OPENAI_API_KEY env var)"
    )
    
    parser.add_argument(
        "--anthropic-key",
        type=str,
        default=os.environ.get("ANTHROPIC_API_KEY"),
        help="Anthropic API key (default: from ANTHROPIC_API_KEY env var)"
    )
    
    parser.add_argument(
        "--save-metrics",
        action="store_true",
        help="Save performance metrics to a JSON file"
    )
    
    return parser.parse_args()


async def main():
    """Main entry point for the CLI."""
    args = parse_args()
    
    # Validate API keys
    if not args.openai_key:
        logger.error("OpenAI API key is required. Set OPENAI_API_KEY environment variable or use --openai-key.")
        sys.exit(1)
        
    if not args.anthropic_key:
        logger.error("Anthropic API key is required. Set ANTHROPIC_API_KEY environment variable or use --anthropic-key.")
        sys.exit(1)
    
    # Prepare arguments for the video generator
    kwargs = {}
    
    if args.category:
        kwargs["category"] = args.category
        
    if args.difficulty:
        kwargs["difficulty_level"] = args.difficulty
        
    if args.max_duration:
        kwargs["max_duration"] = args.max_duration
        
    if args.focus:
        kwargs["focus_areas"] = args.focus
    
    # Generate the video
    try:
        logger.info(f"Generating video for query: {args.query}")
        
        video_path, metrics = await generate_math_video(
            query=args.query,
            openai_api_key=args.openai_key,
            anthropic_api_key=args.anthropic_key,
            **kwargs
        )
        
        logger.info(f"Video generation completed successfully!")
        logger.info(f"Video saved to: {video_path}")
        
        # Save metrics if requested
        if args.save_metrics:
            metrics_path = Path(args.output_dir) / "metrics.json"
            with open(metrics_path, "w") as f:
                json.dump(metrics, f, indent=2)
            logger.info(f"Performance metrics saved to: {metrics_path}")
            
        # Print summary stats
        total_time = metrics["total_duration"]
        logger.info(f"Total generation time: {total_time:.2f} seconds")
        
        if "stage_durations" in metrics and "stage_times" in metrics["stage_durations"]:
            logger.info("Time breakdown by stage:")
            for stage, duration in metrics["stage_durations"]["stage_times"].items():
                percentage = duration / total_time * 100
                logger.info(f"  - {stage}: {duration:.2f}s ({percentage:.1f}%)")
        
    except Exception as e:
        logger.error(f"Error generating video: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main()) 