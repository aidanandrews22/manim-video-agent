import os
import json
from pathlib import Path
from typing import Dict, Optional

def generate_code_prompt(
    scene_id: str,
    scene_title: str,
    narration: str,
    animation_plan: dict,
    context_examples: Optional[str] = None
) -> str:
    """
    Generate a comprehensive prompt by combining a detailed base prompt
    and additional prompts from the prompt directory.

    Args:
        scene_id: Identifier for the scene.
        scene_title: Title of the scene.
        narration: Narration script provided as audio.
        animation_plan: Structured JSON animation plan.
        context_examples: Optional examples for context learning.

    Returns:
        A string containing the combined and integrated prompts.
    """
    # Base Prompt
    template = f""
    with open(Path(__file__).parent / "prompt" / "prompt_code_generation.txt", 'r') as file:
        template = file.read()
    
    # Pre-process the template to replace json.dumps expression
    animation_plan_json = json.dumps(animation_plan, indent=2)
    template = template.replace('{json.dumps(animation_plan, indent=2)}', '{animation_plan_json}')
    
    # Extract scene number from scene_id (assuming scene_id format like "scene1", "scene2", etc.)
    scene_number = ''.join(filter(str.isdigit, scene_id))
    if not scene_number:
        scene_number = "1"  # Default to 1 if no number is found
        
    # Format the template with the provided values
    combined_prompt = template.format(
        scene_id=scene_id, 
        scene_title=scene_title,
        scene_number=scene_number,
        narration=narration, 
        animation_plan_json=animation_plan_json
    )

    # Directory containing additional prompt files
    prompt_dir = Path(__file__).parent / "prompt"
    prompts: Dict[str, str] = {}

    # Load additional prompts
    for file_path in prompt_dir.glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            prompts[file_path.name] = f.read().strip()

    # Integrate additional prompts meaningfully
    integration_sections = [
        ("prompt_manim_cheatsheet.txt", "# Manim Cheatsheet"),
        ("code_color_cheatsheet.txt", "# Color Cheatsheet"),
        ("code_limit.txt", "# Frame Dimensions and Limits"),
        ("code_background.txt", "# Background Information"),
        ("code_font_size.txt", "# Font Size Guidelines"),
    ]

    for filename, section_title in integration_sections:
        if filename in prompts:
            combined_prompt += f"\n\n{section_title}\n{prompts[filename]}"

    # Context Learning Examples Integration
    if "prompt_context_learning_code.txt" in prompts and context_examples:
        context_prompt = prompts["prompt_context_learning_code.txt"].replace("{examples}", context_examples)
        combined_prompt += f"\n\n# Example Code\n{context_prompt}"

    return combined_prompt.strip()
