"""
FastAPI server for the Manim Video Generator.
"""

import os
import json
import asyncio
import uuid
from typing import Dict, Any, Optional, List
from pathlib import Path

from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends, status, Query
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from src.core.pipeline import generate_math_video
from src.core.input_processor import MathQuery
from src.config.config import Config
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Manim Video Generator API",
    description="API for generating educational mathematical videos with Manim",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Track active jobs
active_jobs = {}


class VideoRequest(BaseModel):
    """Request model for video generation."""
    query: str = Field(..., min_length=5, description="Mathematical topic or problem to explain")
    category: Optional[str] = Field(None, description="Category of mathematical content")
    difficulty_level: Optional[str] = Field(None, description="Target difficulty level")
    max_duration: Optional[int] = Field(None, ge=30, le=600, description="Maximum video duration in seconds")
    focus_areas: Optional[List[str]] = Field(None, description="Specific areas to focus on")


class JobStatus(BaseModel):
    """Status model for video generation jobs."""
    job_id: str
    status: str
    progress: Optional[float] = None
    message: Optional[str] = None
    video_path: Optional[str] = None
    error: Optional[str] = None
    metrics: Optional[Dict[str, Any]] = None


def get_api_keys():
    """Get API keys from environment variables."""
    openai_key = os.environ.get("OPENAI_API_KEY")
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    
    if not openai_key:
        logger.error("OPENAI_API_KEY environment variable is not set")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="OpenAI API key not configured on server"
        )
        
    if not anthropic_key:
        logger.error("ANTHROPIC_API_KEY environment variable is not set")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Anthropic API key not configured on server"
        )
        
    return {"openai_key": openai_key, "anthropic_key": anthropic_key}


async def generate_video_task(job_id: str, request: VideoRequest, api_keys: Dict[str, str]):
    """Background task for video generation."""
    try:
        # Update job status
        active_jobs[job_id]["status"] = "processing"
        active_jobs[job_id]["progress"] = 0.0
        active_jobs[job_id]["message"] = "Starting video generation"
        
        # Convert request to kwargs
        kwargs = request.dict(exclude_unset=True)
        query = kwargs.pop("query")
        
        # Generate the video
        video_path, metrics = await generate_math_video(
            query=query,
            openai_api_key=api_keys["openai_key"],
            anthropic_api_key=api_keys["anthropic_key"],
            **kwargs
        )
        
        # Update job status
        active_jobs[job_id]["status"] = "completed"
        active_jobs[job_id]["progress"] = 100.0
        active_jobs[job_id]["message"] = "Video generation completed"
        active_jobs[job_id]["video_path"] = video_path
        active_jobs[job_id]["metrics"] = metrics
        
        logger.info(f"Job {job_id} completed successfully")
        
    except Exception as e:
        logger.error(f"Error in job {job_id}: {str(e)}")
        
        # Update job status
        active_jobs[job_id]["status"] = "failed"
        active_jobs[job_id]["message"] = "Video generation failed"
        active_jobs[job_id]["error"] = str(e)


@app.post("/generate", response_model=JobStatus, status_code=status.HTTP_202_ACCEPTED)
async def create_video(
    request: VideoRequest,
    background_tasks: BackgroundTasks,
    api_keys: Dict[str, str] = Depends(get_api_keys)
):
    """
    Start a video generation job.
    
    The job will run in the background, and the status can be checked with the /status endpoint.
    """
    # Generate a unique job ID
    job_id = str(uuid.uuid4())
    
    # Initialize job status
    active_jobs[job_id] = {
        "job_id": job_id,
        "status": "queued",
        "progress": 0.0,
        "message": "Job queued",
        "video_path": None,
        "error": None,
        "metrics": None
    }
    
    # Start the video generation in the background
    background_tasks.add_task(generate_video_task, job_id, request, api_keys)
    
    logger.info(f"Job {job_id} queued for query: {request.query}")
    
    return JobStatus(**active_jobs[job_id])


@app.get("/status/{job_id}", response_model=JobStatus)
async def get_job_status(job_id: str):
    """
    Get the status of a video generation job.
    """
    if job_id not in active_jobs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job {job_id} not found"
        )
        
    return JobStatus(**active_jobs[job_id])


@app.get("/video/{job_id}")
async def get_video(job_id: str):
    """
    Get the generated video for a completed job.
    """
    if job_id not in active_jobs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job {job_id} not found"
        )
        
    job = active_jobs[job_id]
    
    if job["status"] != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Job {job_id} is not completed yet. Current status: {job['status']}"
        )
        
    if not job["video_path"] or not os.path.exists(job["video_path"]):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Video file not found for job {job_id}"
        )
        
    return FileResponse(
        path=job["video_path"],
        media_type="video/mp4",
        filename=os.path.basename(job["video_path"])
    )


@app.get("/metrics/{job_id}")
async def get_metrics(job_id: str):
    """
    Get the performance metrics for a completed job.
    """
    if job_id not in active_jobs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job {job_id} not found"
        )
        
    job = active_jobs[job_id]
    
    if job["status"] != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Job {job_id} is not completed yet. Current status: {job['status']}"
        )
        
    if not job["metrics"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Metrics not found for job {job_id}"
        )
        
    return job["metrics"]


@app.get("/")
async def root():
    """API root endpoint."""
    return {
        "message": "Manim Video Generator API",
        "docs": "/docs",
        "status": "operational"
    }


# Run with: uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload 