# Manim Video Agent

A high-performance multimodal video generator for educational math videos, leveraging AI to create engaging animations with minimal human input.

## Overview

Manim Video Agent automates the creation of educational mathematics videos by:

1. Solving mathematical problems using OpenAI's o3-mini model
2. Breaking down the video into scenes with o3-mini
3. Generating detailed scripts and animation plans for each scene with Google's Gemini 1.5 Flash
4. Producing Manim Python code for each scene with Anthropic's Claude 3.7 Sonnet
5. Creating audio with Kokoro TTS
6. Rendering each scene with Manim and syncing with audio
7. Stitching scenes together into a cohesive final video

## Features

- **Mathematical Problem Solving**: Leverages OpenAI's o3-mini for efficient, accurate mathematical reasoning
- **Scene-Based Workflow**: Breaks videos down into logical scenes for more modular processing
- **Multi-Model AI Pipeline**: Uses specialized AI models for each part of the process:
  - OpenAI's o3-mini for mathematical problem-solving and scene planning
  - Google's Gemini 1.5 Flash for script and animation planning
  - Anthropic's Claude 3.7 Sonnet for Manim code generation
- **Audio-Visual Synchronization**: Ensures perfect timing between narration and animations
- **Efficient Caching**: Implements a robust caching system to avoid redundant API calls
- **Modular Architecture**: Designed with clean separation of concerns for easy extension

## Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- Anthropic API key
- Google Generative AI API key
- Manim animation library
- FFmpeg
- Kokoro TTS setup (for voice generation)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/manim-video-agent.git
   cd manim-video-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   export ANTHROPIC_API_KEY="your_anthropic_api_key"
   export GEMINI_API_KEY="your_gemini_api_key"
   export KOKORO_MODEL_PATH="path/to/kokoro/model"
   export KOKORO_VOICES_PATH="path/to/kokoro/voices"
   export KOKORO_DEFAULT_VOICE="your_preferred_voice"
   export KOKORO_DEFAULT_SPEED="1.0"
   export KOKORO_DEFAULT_LANG="en"
   ```

## Usage

### Command Line Interface

Generate a video from a mathematical problem:

```bash
python -m src.main "Solve the quadratic equation x^2 - 5x + 6 = 0" --output ./output
```

Options:
- `--output`, `-o`: Directory to save the generated files (default: "output")
- `--no-cache`: Disable caching of AI responses

### Output Files

The program generates the following files in the output directory:

- `solution.txt`: The step-by-step solution to the mathematical problem
- `scene_plan.json`: The structured scene-by-scene plan
- `scenes.json`: The complete list of scenes with their details
- `final_video.mp4`: The final rendered video
- Scene-specific files in subdirectories:
  - `scene1/script.txt`: The narration script for Scene 1
  - `scene1/animation_plan.json`: The animation plan for Scene 1
  - `scene1/scene1.py`: The Manim Python code for Scene 1
  - `scene1/scene1_audio.mp3`: The audio file for Scene 1
  - `scene1/scene1_synced.mp4`: The final synced video for Scene 1

## Project Structure

```
manim-video-agent/
├── src/
│   ├── config/
│   │   └── config.py         # Configuration management
│   ├── core/
│   │   ├── ai_manager.py     # AI model interaction
│   │   └── animation_planner.py  # Animation planning
│   ├── utils/
│   │   ├── logging_utils.py  # Logging utilities
│   │   ├── kokoro_voiceover.py  # Voice generation
│   │   └── video_utils.py    # Video processing
│   ├── main.py               # Main entry point
│   ├── api.py                # API endpoints
│   └── cli.py                # Command line interface
├── tests/                    # Unit and integration tests
├── .env.example              # Example environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Implementation Status

### Completed

- [x] Mathematical Problem Solving with o3-mini
- [x] Scene-based planning with o3-mini
- [x] Script and animation plan generation with Gemini 1.5 Flash
- [x] Manim code generation with Claude 3.7 Sonnet
- [x] Kokoro TTS integration for voice generation
- [x] Video processing pipeline
- [x] Audio-visual synchronization
- [x] Scene stitching for final video

### In Progress

- [ ] Web interface for video creation
- [ ] Support for more complex mathematical problems
- [ ] Custom style templates
- [ ] Performance optimizations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Manim Community](https://www.manim.community/) for the animation library
- OpenAI, Anthropic, and Google for their powerful AI models
- Kokoro TTS for voice generation capability
