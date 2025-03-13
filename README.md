# Manim Video Agent

A high-performance multimodal video generator for educational math videos, leveraging AI to create engaging animations with minimal human input.

## Overview

Manim Video Agent automates the creation of educational mathematics videos by:

1. Solving mathematical problems using OpenAI's o3-mini model
2. Creating detailed animation plans with GPT-4o
3. Generating natural-sounding narration scripts with Claude 3.7 Sonnet
4. Producing Manim Python code to render the animations
5. Rendering the final video with synchronized narration

## Features

- **Mathematical Problem Solving**: Leverages OpenAI's o3-mini for efficient, accurate mathematical reasoning
- **Intelligent Animation Planning**: Uses GPT-4o to create structured animation plans with scene breakdown and timing estimation
- **Natural Narration**: Generates human-like narration scripts with Claude 3.7 Sonnet
- **Manim Code Generation**: Automatically produces Python code using the Manim animation library
- **Efficient Caching**: Implements a robust caching system to avoid redundant API calls
- **Modular Architecture**: Designed with clean separation of concerns for easy extension

## Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- Anthropic API key
- Manim animation library
- FFmpeg

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
- `animation_plan.json`: The structured animation plan
- `script.json`: The narration script
- `animation.py`: The Manim Python code
- (When rendering is implemented) `video.mp4`: The final rendered video

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
│   │   └── logging_utils.py  # Logging utilities
│   └── main.py               # Main entry point
├── tests/                    # Unit and integration tests
├── .env.example              # Example environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Implementation Status

### Completed

- [x] Mathematical Problem Solving with o3-mini
- [x] Animation Planning with GPT-4o
- [x] Caching layer for AI responses
- [x] Scene breakdown algorithm
- [x] Timing estimation system
- [x] Templates for common mathematical visualizations

### In Progress

- [ ] Script Generation with Claude 3.7 Sonnet
- [ ] Manim Code Generation with Claude 3.7 Sonnet
- [ ] Video Rendering Pipeline
- [ ] User Interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Manim Community](https://www.manim.community/) for the animation library
- OpenAI and Anthropic for their powerful AI models
