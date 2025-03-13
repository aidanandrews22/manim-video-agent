"""
Logging utilities for the Manim Video Generator.
"""

import os
import logging
import colorlog
from concurrent_log_handler import ConcurrentRotatingFileHandler
from pathlib import Path

# Create logs directory if it doesn't exist
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Set up logging configuration
def get_logger(name, log_level=logging.INFO):
    """
    Get a configured logger instance.
    
    Args:
        name: Logger name, typically __name__
        log_level: Logging level
        
    Returns:
        Configured logger
    """
    logger = logging.getLogger(name)
    
    # Only configure logger once
    if logger.handlers:
        return logger
        
    logger.setLevel(log_level)
    
    # Configure console handler with colorful output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    
    # Add colors to different log levels
    color_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )
    console_handler.setFormatter(color_formatter)
    logger.addHandler(console_handler)
    
    # Configure file handler with rotating log files
    file_handler = ConcurrentRotatingFileHandler(
        filename=logs_dir / f"{name.split('.')[-1]}.log",
        mode='a',
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(log_level)
    
    # Use standard formatting for log files (without colors)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    return logger


class ProgressLogger:
    """
    Specialized logger for tracking progress of pipeline stages.
    """
    
    def __init__(self, total_stages):
        """
        Initialize a progress logger.
        
        Args:
            total_stages: Total number of stages in the pipeline
        """
        self.logger = get_logger("progress")
        self.total_stages = total_stages
        self.current_stage = 0
        self.stage_times = {}
        self.start_times = {}
        
    def start_stage(self, stage_name):
        """
        Record the start of a pipeline stage.
        
        Args:
            stage_name: Name of the stage
        """
        import time
        self.current_stage += 1
        self.start_times[stage_name] = time.time()
        
        progress = (self.current_stage - 1) / self.total_stages * 100
        self.logger.info(f"[{progress:.1f}%] Starting stage: {stage_name} ({self.current_stage}/{self.total_stages})")
        
    def end_stage(self, stage_name, success=True):
        """
        Record the end of a pipeline stage.
        
        Args:
            stage_name: Name of the stage
            success: Whether the stage completed successfully
        """
        import time
        end_time = time.time()
        if stage_name in self.start_times:
            elapsed = end_time - self.start_times[stage_name]
            self.stage_times[stage_name] = elapsed
            
            progress = self.current_stage / self.total_stages * 100
            status = "Completed" if success else "Failed"
            
            self.logger.info(f"[{progress:.1f}%] {status} stage: {stage_name} in {elapsed:.2f}s")
        else:
            self.logger.warning(f"Ending untracked stage: {stage_name}")
            
    def get_performance_summary(self):
        """
        Get a summary of performance timing.
        
        Returns:
            Dictionary with stage timing information
        """
        total_time = sum(self.stage_times.values())
        
        summary = {
            "total_time": total_time,
            "stage_times": self.stage_times,
            "stage_percentages": {
                stage: (time / total_time * 100) 
                for stage, time in self.stage_times.items()
            }
        }
        
        return summary 