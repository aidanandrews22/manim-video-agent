#!/usr/bin/env python3
"""
Runner script for the Manim Video Generator.

This script provides a simple interface to run either the CLI or API server.
"""

import os
import sys
import argparse
import subprocess
import asyncio
from pathlib import Path

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run the Manim Video Generator in CLI or API mode."
    )
    
    parser.add_argument(
        "mode",
        choices=["cli", "api"],
        help="Run mode: 'cli' for command-line interface, 'api' for API server"
    )
    
    # CLI mode arguments
    parser.add_argument(
        "--query",
        type=str,
        help="Mathematical topic or problem to explain (CLI mode only)"
    )
    
    parser.add_argument(
        "--category",
        type=str,
        choices=["theorem", "problem", "concept", "definition", "proof"],
        help="Category of mathematical content (CLI mode only)"
    )
    
    parser.add_argument(
        "--difficulty",
        type=str,
        choices=["elementary", "high school", "undergraduate", "graduate"],
        help="Target difficulty level (CLI mode only)"
    )
    
    # API mode arguments
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host to bind the API server to (API mode only)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the API server to (API mode only)"
    )
    
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for the API server (API mode only)"
    )
    
    return parser.parse_args()


def run_cli(args):
    """Run the CLI with the provided arguments."""
    from src.cli import main
    
    # Reconstruct sys.argv for the CLI module
    sys.argv = [sys.argv[0]]
    
    if not args.query:
        print("Error: --query is required for CLI mode")
        sys.exit(1)
        
    sys.argv.append(args.query)
    
    if args.category:
        sys.argv.extend(["--category", args.category])
        
    if args.difficulty:
        sys.argv.extend(["--difficulty", args.difficulty])
    
    # Run the CLI main function
    asyncio.run(main())


def run_api(args):
    """Run the API server with the provided arguments."""
    reload_flag = "--reload" if args.reload else ""
    
    # Run uvicorn directly
    cmd = f"uvicorn src.api:app --host {args.host} --port {args.port} {reload_flag}"
    print(f"Starting API server: {cmd}")
    
    try:
        subprocess.run(cmd, shell=True, check=True)
    except KeyboardInterrupt:
        print("API server stopped")
    except subprocess.CalledProcessError as e:
        print(f"Error starting API server: {e}")
        sys.exit(1)


def check_environment():
    """Check if the environment is properly set up."""
    # Check for required API keys
    missing_keys = []
    
    if not os.environ.get("OPENAI_API_KEY"):
        missing_keys.append("OPENAI_API_KEY")
        
    if not os.environ.get("ANTHROPIC_API_KEY"):
        missing_keys.append("ANTHROPIC_API_KEY")
    
    if missing_keys:
        print(f"Error: Missing required environment variables: {', '.join(missing_keys)}")
        print("Please set these variables before running the application.")
        sys.exit(1)
    
    # Check for required directories
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    models_dir = Path("models")
    if not models_dir.exists() or not any(models_dir.iterdir()):
        print("Warning: Models directory is empty or does not exist.")
        print("Make sure to download the Kokoro TTS model files (kokoro-v0_19.onnx and voices.bin) to the models/ directory.")


def main():
    """Main entry point."""
    # Parse arguments
    args = parse_args()
    
    # Check environment
    check_environment()
    
    # Run in the selected mode
    if args.mode == "cli":
        run_cli(args)
    else:  # args.mode == "api"
        run_api(args)


if __name__ == "__main__":
    main() 