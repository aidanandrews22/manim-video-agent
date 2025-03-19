"""
Animation Planning Module for Manim Video Generator.

This module provides advanced planning capabilities for mathematical animations,
including scene breakdown, timing estimation, and templates for common visualizations.
"""

import json
from typing import Dict, Any, List, Optional, Tuple
from pydantic import BaseModel, Field, validator
import math

from src.utils.logging_utils import get_logger

logger = get_logger(__name__)


class VisualElement(BaseModel):
    """Schema for a visual element in the animation."""
    type: str = Field(..., description="Type of visual element (text, equation, shape, graph, etc.)")
    content: str = Field(..., description="Specific content to display")
    animation: str = Field(..., description="Type of animation to use (FadeIn, Transform, etc.)")
    duration: float = Field(..., description="Duration in seconds")
    sync_with_narration: Optional[str] = Field(None, description="Text that should be spoken during this element")


class Scene(BaseModel):
    """Schema for a scene in the animation."""
    id: str = Field(..., description="Unique identifier for the scene")
    title: str = Field(..., description="Title of the scene")
    duration: float = Field(..., description="Duration in seconds")
    narration: str = Field(..., description="Script for the scene")
    animation_plan: Dict[str, Any] = Field(..., description="Animation plan for the scene")
    original_query: str = Field(..., description="Original query provided by the user")
    original_solution: str = Field(..., description="Original solution provided by the AI")
    manim_code: Optional[str] = Field(None, description="Manim code for the scene")
    audio_file: Optional[str] = Field(None, description="Path to the generated audio file")
    video_file: Optional[str] = Field(None, description="Path to the generated video file")


class Section(BaseModel):
    """Schema for a section in the animation plan."""
    id: str = Field(..., description="Unique identifier for the section")
    title: str = Field(..., description="Title of the section")
    duration: float = Field(..., description="Duration in seconds")
    narration_summary: str = Field(..., description="Summary of what will be explained in this section")
    visual_elements: List[VisualElement] = Field(..., description="Visual elements in this section")
    
    @validator('duration')
    def validate_duration(cls, v, values):
        """Validate that the section duration matches the sum of visual elements."""
        if 'visual_elements' in values and values['visual_elements']:
            total_element_duration = sum(element.duration for element in values['visual_elements'])
            # Allow for small differences due to floating point precision
            if abs(v - total_element_duration) > 0.5:
                logger.warning(f"Section '{values.get('id', 'unknown')}' duration ({v}s) doesn't match sum of visual elements ({total_element_duration}s)")
                # Adjust the section duration to match the sum of visual elements
                return total_element_duration
        return v


class VisualStyle(BaseModel):
    """Schema for the visual style of the animation."""
    color_theme: str = Field(..., description="Color theme (dark/light)")
    font_size: str = Field(..., description="Font size (small/medium/large)")
    background_color: str = Field(..., description="Background color in hex format")
    accent_color: str = Field(..., description="Accent color in hex format")


class AnimationPlan(BaseModel):
    """Schema for the complete animation plan."""
    title: str = Field(..., description="Title of the video")
    sections: List[Section] = Field(..., description="List of sections in the animation")
    scenes: Optional[List[Scene]] = Field(None, description="List of scenes in the animation")
    estimated_duration: float = Field(..., description="Estimated duration in seconds")
    visual_style: VisualStyle = Field(..., description="Visual style guidelines")
    
    @validator('estimated_duration')
    def validate_estimated_duration(cls, v, values):
        """Validate that the estimated duration matches the sum of section durations."""
        if 'sections' in values and values['sections']:
            total_section_duration = sum(section.duration for section in values['sections'])
            # Allow for small differences due to floating point precision
            if abs(v - total_section_duration) > 1.0:
                logger.warning(f"Estimated duration ({v}s) doesn't match sum of sections ({total_section_duration}s)")
                # Adjust the estimated duration to match the sum of sections
                return total_section_duration
        return v


class SceneBreakdownAlgorithm:
    """
    Algorithm for breaking down complex topics into logical segments.
    """
    
    @staticmethod
    def breakdown_explanation(explanation: str, max_sections: int = 5) -> List[Dict[str, Any]]:
        """
        Break down a mathematical explanation into logical sections.
        
        Args:
            explanation: The mathematical explanation text
            max_sections: Maximum number of sections to create
            
        Returns:
            List of section dictionaries with id, title, and content
        """
        # Split the explanation into paragraphs
        paragraphs = [p.strip() for p in explanation.split('\n\n') if p.strip()]
        
        # If there are too few paragraphs, treat each as a section
        if len(paragraphs) <= max_sections:
            return [
                {
                    "id": f"section{i+1}",
                    "title": _extract_title(paragraph, i),
                    "content": paragraph
                }
                for i, paragraph in enumerate(paragraphs)
            ]
        
        # If there are too many paragraphs, group them into sections
        sections = []
        paragraphs_per_section = math.ceil(len(paragraphs) / max_sections)
        
        for i in range(0, len(paragraphs), paragraphs_per_section):
            section_paragraphs = paragraphs[i:i+paragraphs_per_section]
            section_content = '\n\n'.join(section_paragraphs)
            section_id = f"section{len(sections)+1}"
            section_title = _extract_title(section_paragraphs[0], len(sections))
            
            sections.append({
                "id": section_id,
                "title": section_title,
                "content": section_content
            })
        
        return sections


def _extract_title(text: str, fallback_index: int) -> str:
    """
    Extract a title from the first sentence or line of text.
    
    Args:
        text: The text to extract a title from
        fallback_index: Index to use in fallback title
        
    Returns:
        A suitable title
    """
    # Try to get the first sentence
    if '.' in text[:100]:
        first_sentence = text.split('.')[0].strip()
        if 10 <= len(first_sentence) <= 50:
            return first_sentence
    
    # Try to get the first line
    if '\n' in text[:100]:
        first_line = text.split('\n')[0].strip()
        if 10 <= len(first_line) <= 50:
            return first_line
    
    # If the first sentence/line is too short or too long, use a generic title
    return f"Section {fallback_index + 1}"


class TimingEstimator:
    """
    System for estimating durations of animations and narrations.
    """
    
    # Average reading speed in words per minute
    READING_SPEED = 150
    
    # Base durations for different animation types in seconds
    ANIMATION_DURATIONS = {
        "FadeIn": 1.0,
        "FadeOut": 1.0,
        "Write": 2.0,
        "Transform": 1.5,
        "ReplacementTransform": 1.5,
        "Create": 1.5,
        "DrawBorderThenFill": 2.0,
        "ShowCreation": 1.5,
        "Indicate": 1.0,
        "CircleIndicate": 1.0,
        "ShowPassingFlash": 1.0,
        "ShowCreationThenDestruction": 2.0,
        "ApplyMethod": 1.0,
        "default": 1.5
    }
    
    @classmethod
    def estimate_narration_duration(cls, text: str) -> float:
        """
        Estimate the duration of narration based on word count.
        
        Args:
            text: The narration text
            
        Returns:
            Estimated duration in seconds
        """
        # Count words
        word_count = len(text.split())
        
        # Calculate duration based on reading speed
        duration_minutes = word_count / cls.READING_SPEED
        duration_seconds = duration_minutes * 60
        
        # Add a small buffer for pauses
        buffer_seconds = word_count / 50  # Add 1 second for every 50 words
        
        return duration_seconds + buffer_seconds
    
    @classmethod
    def estimate_animation_duration(cls, animation_type: str, content: str) -> float:
        """
        Estimate the duration of an animation based on type and content.
        
        Args:
            animation_type: The type of animation
            content: The content being animated
            
        Returns:
            Estimated duration in seconds
        """
        # Get base duration for the animation type
        base_duration = cls.ANIMATION_DURATIONS.get(animation_type, cls.ANIMATION_DURATIONS["default"])
        
        # Adjust based on content length
        content_factor = 1.0
        if len(content) > 100:
            content_factor = 1.5
        elif len(content) > 50:
            content_factor = 1.2
        
        return base_duration * content_factor
    
    @classmethod
    def estimate_section_duration(cls, narration: str, visual_elements: List[Dict[str, Any]]) -> float:
        """
        Estimate the total duration of a section based on narration and visual elements.
        
        Args:
            narration: The narration text for the section
            visual_elements: List of visual elements in the section
            
        Returns:
            Estimated duration in seconds
        """
        narration_duration = cls.estimate_narration_duration(narration)
        
        # Sum up the durations of visual elements
        animation_duration = sum(
            cls.estimate_animation_duration(element.get("animation", "default"), element.get("content", ""))
            for element in visual_elements
        )
        
        # The section duration should be the longer of narration or animation
        # plus a small buffer for transitions
        return max(narration_duration, animation_duration) + 2.0


class VisualizationTemplates:
    """
    Templates for common mathematical visualizations.
    """
    
    @staticmethod
    def get_template(concept_type: str) -> List[Dict[str, Any]]:
        """
        Get a template for a specific mathematical concept.
        
        Args:
            concept_type: Type of mathematical concept
            
        Returns:
            List of visual elements for the template
        """
        templates = {
            "theorem": [
                {
                    "type": "text",
                    "content": "Theorem Statement",
                    "animation": "Write",
                    "duration": 2.0
                },
                {
                    "type": "text",
                    "content": "Key Insight",
                    "animation": "FadeIn",
                    "duration": 1.5
                },
                {
                    "type": "equation",
                    "content": "Mathematical Formulation",
                    "animation": "Write",
                    "duration": 2.5
                },
                {
                    "type": "graph",
                    "content": "Visual Representation",
                    "animation": "Create",
                    "duration": 3.0
                },
                {
                    "type": "text",
                    "content": "Implications",
                    "animation": "FadeIn",
                    "duration": 1.5
                }
            ],
            "proof": [
                {
                    "type": "text",
                    "content": "Theorem to Prove",
                    "animation": "Write",
                    "duration": 2.0
                },
                {
                    "type": "text",
                    "content": "Proof Strategy",
                    "animation": "FadeIn",
                    "duration": 1.5
                },
                {
                    "type": "equation",
                    "content": "Starting Point",
                    "animation": "Write",
                    "duration": 2.0
                },
                {
                    "type": "equation",
                    "content": "Step 1",
                    "animation": "Transform",
                    "duration": 2.0
                },
                {
                    "type": "equation",
                    "content": "Step 2",
                    "animation": "Transform",
                    "duration": 2.0
                },
                {
                    "type": "equation",
                    "content": "Final Result",
                    "animation": "Transform",
                    "duration": 2.0
                },
                {
                    "type": "text",
                    "content": "QED",
                    "animation": "FadeIn",
                    "duration": 1.0
                }
            ],
            "concept": [
                {
                    "type": "text",
                    "content": "Concept Introduction",
                    "animation": "Write",
                    "duration": 2.0
                },
                {
                    "type": "text",
                    "content": "Intuitive Explanation",
                    "animation": "FadeIn",
                    "duration": 2.0
                },
                {
                    "type": "graph",
                    "content": "Visual Representation",
                    "animation": "Create",
                    "duration": 3.0
                },
                {
                    "type": "equation",
                    "content": "Formal Definition",
                    "animation": "Write",
                    "duration": 2.5
                },
                {
                    "type": "text",
                    "content": "Examples",
                    "animation": "FadeIn",
                    "duration": 2.0
                },
                {
                    "type": "text",
                    "content": "Applications",
                    "animation": "FadeIn",
                    "duration": 1.5
                }
            ],
            "problem": [
                {
                    "type": "text",
                    "content": "Problem Statement",
                    "animation": "Write",
                    "duration": 2.0
                },
                {
                    "type": "text",
                    "content": "Key Insight",
                    "animation": "FadeIn",
                    "duration": 1.5
                },
                {
                    "type": "equation",
                    "content": "Step 1",
                    "animation": "Write",
                    "duration": 2.0
                },
                {
                    "type": "equation",
                    "content": "Step 2",
                    "animation": "Transform",
                    "duration": 2.0
                },
                {
                    "type": "equation",
                    "content": "Step 3",
                    "animation": "Transform",
                    "duration": 2.0
                },
                {
                    "type": "equation",
                    "content": "Final Answer",
                    "animation": "Transform",
                    "duration": 2.0
                }
            ]
        }
        
        return templates.get(concept_type, templates["concept"])


class AnimationPlanner:
    """
    Advanced animation planner that enhances the basic plan from the AI.
    """
    
    def __init__(self):
        """Initialize the animation planner."""
        self.scene_breakdown = SceneBreakdownAlgorithm()
        self.timing_estimator = TimingEstimator()
        self.templates = VisualizationTemplates()
    
    def enhance_plan(self, basic_plan: Dict[str, Any], explanation: str, category: str) -> AnimationPlan:
        """
        Enhance a basic animation plan with improved timing and templates.
        
        Args:
            basic_plan: The basic animation plan from the AI
            explanation: The mathematical explanation
            category: The category of mathematical content
            
        Returns:
            An enhanced animation plan
        """
        # Create a copy of the basic plan to avoid modifying the original
        enhanced_plan = dict(basic_plan)
        
        # Enhance each section
        for i, section in enumerate(enhanced_plan.get("sections", [])):
            # Ensure section has an ID
            if "id" not in section:
                section["id"] = f"section{i+1}"
            
            # Apply templates for visual elements if none exist
            if not section.get("visual_elements"):
                section["visual_elements"] = self.templates.get_template(category)
            
            # Improve timing estimates
            if "narration_summary" in section:
                narration = section["narration_summary"]
                visual_elements = section.get("visual_elements", [])
                
                # Update duration based on narration and visual elements
                section["duration"] = self.timing_estimator.estimate_section_duration(
                    narration, visual_elements
                )
        
        # Update the overall estimated duration
        if "sections" in enhanced_plan:
            total_duration = sum(section.get("duration", 0) for section in enhanced_plan["sections"])
            enhanced_plan["estimated_duration"] = total_duration
        
        # Validate and return the enhanced plan
        return AnimationPlan(**enhanced_plan)
    
    def create_plan_from_explanation(self, explanation: str, category: str, title: str) -> AnimationPlan:
        """
        Create a complete animation plan directly from an explanation.
        
        Args:
            explanation: The mathematical explanation
            category: The category of mathematical content
            title: The title for the animation
            
        Returns:
            A complete animation plan
        """
        # Break down the explanation into sections
        sections_data = self.scene_breakdown.breakdown_explanation(explanation)
        
        # Create sections with visual elements and timing
        sections = []
        for section_data in sections_data:
            # Get template visual elements for this category
            visual_elements = self.templates.get_template(category)
            
            # Estimate duration based on content and visual elements
            duration = self.timing_estimator.estimate_section_duration(
                section_data["content"], visual_elements
            )
            
            # Create the section
            section = {
                "id": section_data["id"],
                "title": section_data["title"],
                "duration": duration,
                "narration_summary": section_data["content"],
                "visual_elements": visual_elements
            }
            
            sections.append(section)
        
        # Calculate total duration
        total_duration = sum(section["duration"] for section in sections)
        
        # Create the visual style
        visual_style = {
            "color_theme": "dark",
            "font_size": "medium",
            "background_color": "#1C1C1C",
            "accent_color": "#3B82F6"
        }
        
        # Create the complete plan
        plan_dict = {
            "title": title,
            "sections": sections,
            "estimated_duration": total_duration,
            "visual_style": visual_style
        }
        
        # Validate and return the plan
        return AnimationPlan(**plan_dict) 