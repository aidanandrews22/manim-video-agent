"""
Pipeline Orchestrator Module for Manim Video Generator.

This module handles the complete end-to-end pipeline for generating
educational math videos, coordinating all the stages from input processing
to final video generation.
"""

import os
import asyncio
import time
from typing import Dict, Any, Optional, List, Tuple
import json
from pathlib import Path

from src.core.input_processor import InputProcessor, MathQuery
from src.core.ai_manager import AIManager, AnimationPlan
from src.core.media_processor import VideoGenerator
from src.utils.logging_utils import get_logger, ProgressLogger
from src.config.config import Config

logger = get_logger(__name__)


class VideoGenerationPipeline:
    """
    End-to-end pipeline for generating educational math videos.
    """
    
    def __init__(self, 
                 openai_api_key: Optional[str] = None,
                 anthropic_api_key: Optional[str] = None,
                 output_dir: str = Config.OUTPUT_DIR):
        """
        Initialize the video generation pipeline.
        
        Args:
            openai_api_key: API key for OpenAI services
            anthropic_api_key: API key for Anthropic services
            output_dir: Directory for output files
        """
        self.input_processor = InputProcessor()
        self.ai_manager = AIManager(openai_api_key, anthropic_api_key)
        self.video_generator = VideoGenerator(output_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)
        
        # Set up progress tracking with 6 main stages
        self.progress = ProgressLogger(6)
        
        # Initialize performance metrics
        self.metrics = {
            "start_time": 0,
            "end_time": 0,
            "total_duration": 0,
            "stage_durations": {},
            "model_usage": {}
        }
    
    async def generate_video(self, query_text: str, **kwargs) -> Tuple[str, Dict[str, Any]]:
        """
        Generate a complete educational math video from a query.
        
        Args:
            query_text: The mathematical topic or problem to explain
            **kwargs: Additional parameters for customization
            
        Returns:
            Tuple of (final_video_path, metrics)
        """
        self.metrics["start_time"] = time.time()
        
        try:
            # Stage 1: Process input
            self.progress.start_stage("input_processing")
            validated_query = self.input_processor.process_query(query_text, **kwargs)
            query_dict = validated_query.to_prompt_dict()
            self.progress.end_stage("input_processing")
            
            # Stage 2: Solve/explain problem with o3-mini
            self.progress.start_stage("problem_solving")
            explanation = await self.ai_manager.solve_math_problem(query_dict)
            self.progress.end_stage("problem_solving")
            
            # Stage 3: Create animation plan with GPT-4o
            self.progress.start_stage("animation_planning")
            animation_plan = await self.ai_manager.create_animation_plan(query_dict, explanation)
            self.progress.end_stage("animation_planning")
            
            # Stage 4: Generate content concurrently (script + manim code)
            self.progress.start_stage("content_generation")
            scripts, manim_code = await self.ai_manager.generate_content_concurrently(
                query_dict, explanation, animation_plan
            )
            self.progress.end_stage("content_generation")
            
            # Save intermediate outputs for debugging/analysis
            self._save_intermediate_outputs(
                query_dict, explanation, animation_plan, scripts, manim_code
            )
            
            # Stage 5: Render animation and synthesize voice
            # Stage 6: Synchronize and compile final video
            # (These are handled internally by video_generator)
            self.progress.start_stage("media_production")
            final_video_path = await self.video_generator.generate_video(
                scripts=scripts,
                manim_code=manim_code,
                title=animation_plan.title,
                metadata={
                    "query": query_dict,
                    "animation_plan": animation_plan.dict(),
                    "generation_timestamp": time.time(),
                    "performance_metrics": self.metrics
                }
            )
            self.progress.end_stage("media_production")
            
            # Finalize metrics
            self.metrics["end_time"] = time.time()
            self.metrics["total_duration"] = self.metrics["end_time"] - self.metrics["start_time"]
            self.metrics["stage_durations"] = self.progress.get_performance_summary()
            self.metrics["model_usage"] = self.ai_manager.get_model_usage()
            
            logger.info(f"Video generation completed in {self.metrics['total_duration']:.2f} seconds")
            logger.info(f"Final video: {final_video_path}")
            
            return final_video_path, self.metrics
            
        except Exception as e:
            logger.error(f"Error in video generation pipeline: {str(e)}")
            self.metrics["error"] = str(e)
            self.metrics["end_time"] = time.time()
            self.metrics["total_duration"] = self.metrics["end_time"] - self.metrics["start_time"]
            raise
    
    def _save_intermediate_outputs(
        self,
        query: Dict[str, Any],
        explanation: str,
        animation_plan: AnimationPlan,
        scripts: Dict[str, str],
        manim_code: str
    ):
        """
        Save intermediate outputs for debugging and analysis.
        
        Args:
            query: The processed query
            explanation: The mathematical explanation
            animation_plan: The structured animation plan
            scripts: The generated narration scripts
            manim_code: The generated Manim code
        """
        # Create a directory for intermediate outputs
        timestamp = int(time.time())
        intermediate_dir = self.output_dir / f"intermediate_{timestamp}"
        intermediate_dir.mkdir(exist_ok=True)
        
        # Save each component
        with open(intermediate_dir / "query.json", "w") as f:
            json.dump(query, f, indent=2)
            
        with open(intermediate_dir / "explanation.txt", "w") as f:
            f.write(explanation)
            
        with open(intermediate_dir / "animation_plan.json", "w") as f:
            json.dump(animation_plan.dict(), f, indent=2)
            
        with open(intermediate_dir / "scripts.json", "w") as f:
            json.dump(scripts, f, indent=2)
            
        with open(intermediate_dir / "manim_code.py", "w") as f:
            f.write(manim_code)
            
        logger.info(f"Saved intermediate outputs to {intermediate_dir}")


async def generate_math_video(
    query: str, 
    openai_api_key: Optional[str] = None,
    anthropic_api_key: Optional[str] = None,
    **kwargs
) -> Tuple[str, Dict[str, Any]]:
    """
    Convenience function for generating a math video.
    
    Args:
        query: Mathematical topic or problem to explain
        openai_api_key: API key for OpenAI services
        anthropic_api_key: API key for Anthropic services
        **kwargs: Additional customization parameters
        
    Returns:
        Tuple of (final_video_path, metrics)
    """
    pipeline = VideoGenerationPipeline(
        openai_api_key=openai_api_key,
        anthropic_api_key=anthropic_api_key
    )
    
    return await pipeline.generate_video(query, **kwargs) 