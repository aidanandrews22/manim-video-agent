"""
Input Processing Module for Manim Video Generator.

This module handles the processing and validation of user input queries,
preparing them for the video generation pipeline.
"""

import re
import time
import heapq
from typing import Dict, Any, Optional, List, Tuple
from pydantic import BaseModel, Field, validator


class MathQuery(BaseModel):
    """
    Validated input query for mathematical content generation.
    """
    query: str = Field(..., min_length=5, description="Mathematical topic or query to be explained")
    category: Optional[str] = Field(None, description="Category of mathematical content (theorem, problem, concept)")
    difficulty_level: Optional[str] = Field(None, description="Target difficulty level (elementary, high school, undergraduate, graduate)")
    max_duration: Optional[int] = Field(None, ge=30, le=600, description="Maximum video duration in seconds")
    focus_areas: Optional[List[str]] = Field(None, description="Specific areas to focus on in the explanation")
    priority: Optional[int] = Field(0, ge=0, le=10, description="Priority level (0-10, higher is more important)")
    
    @validator('query')
    def validate_query(cls, v):
        # Remove excessive whitespace
        v = re.sub(r'\s+', ' ', v).strip()
        
        # Check for overly complex queries
        if len(v) > 300:
            raise ValueError("Query is too long. Please simplify your request.")
            
        return v
    
    @validator('category')
    def validate_category(cls, v):
        if v is not None:
            valid_categories = ['theorem', 'problem', 'concept', 'definition', 'proof']
            v = v.lower()
            if v not in valid_categories:
                raise ValueError(f"Category must be one of {valid_categories}")
        return v
    
    def to_prompt_dict(self) -> Dict[str, Any]:
        """Convert to a dictionary for prompt construction."""
        result = {"query": self.query}
        
        if self.category:
            result["category"] = self.category
            
        if self.difficulty_level:
            result["difficulty_level"] = self.difficulty_level
            
        if self.max_duration:
            result["max_duration"] = self.max_duration
            
        if self.focus_areas:
            result["focus_areas"] = self.focus_areas
            
        return result


class QueryPriorityQueue:
    """
    Priority queue for managing multiple query requests.
    
    Queries are processed based on their priority level and submission time.
    Higher priority queries are processed first, and for queries with the same
    priority, the oldest ones are processed first (FIFO).
    """
    
    def __init__(self):
        """Initialize an empty priority queue."""
        self._queue = []  # List of (priority, timestamp, query_id, query) tuples
        self._counter = 0  # Unique ID for each query
    
    def add_query(self, query: MathQuery) -> str:
        """
        Add a query to the priority queue.
        
        Args:
            query: The validated query to add
            
        Returns:
            A unique ID for the query
        """
        # Invert priority so that higher values are processed first
        # (heapq is a min-heap, so lower values come out first)
        inverted_priority = -1 * (query.priority or 0)
        timestamp = time.time()
        query_id = f"query_{self._counter}"
        self._counter += 1
        
        # Add to the priority queue
        heapq.heappush(self._queue, (inverted_priority, timestamp, query_id, query))
        
        return query_id
    
    def get_next_query(self) -> Tuple[str, MathQuery]:
        """
        Get the next query to process based on priority.
        
        Returns:
            A tuple of (query_id, query) or (None, None) if the queue is empty
        """
        if not self._queue:
            return None, None
            
        _, _, query_id, query = heapq.heappop(self._queue)
        return query_id, query
    
    def peek_next_query(self) -> Tuple[str, MathQuery]:
        """
        Peek at the next query without removing it from the queue.
        
        Returns:
            A tuple of (query_id, query) or (None, None) if the queue is empty
        """
        if not self._queue:
            return None, None
            
        _, _, query_id, query = self._queue[0]
        return query_id, query
    
    def remove_query(self, query_id: str) -> bool:
        """
        Remove a specific query from the queue.
        
        Args:
            query_id: The ID of the query to remove
            
        Returns:
            True if the query was found and removed, False otherwise
        """
        for i, (_, _, qid, _) in enumerate(self._queue):
            if qid == query_id:
                # Remove the item
                self._queue.pop(i)
                # Reheapify
                heapq.heapify(self._queue)
                return True
                
        return False
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._queue) == 0
    
    def size(self) -> int:
        """Get the number of queries in the queue."""
        return len(self._queue)


class InputProcessor:
    """
    Processes and validates user input for the Manim Video Generator.
    """
    
    def __init__(self):
        """Initialize the input processor with a priority queue."""
        self.priority_queue = QueryPriorityQueue()
    
    def process_query(self, query_text: str, **kwargs) -> MathQuery:
        """
        Process and validate the user's query.
        
        Args:
            query_text: The raw query text from the user
            **kwargs: Additional parameters for query processing
            
        Returns:
            A validated MathQuery object
        """
        # Auto-detect query category if not specified
        if 'category' not in kwargs:
            category = self._detect_category(query_text)
            if category:
                kwargs['category'] = category
                
        # Create and validate the query object
        query = MathQuery(query=query_text, **kwargs)
        return query
    
    def _detect_category(self, query_text: str) -> Optional[str]:
        """
        Automatically detect the category of a mathematical query.
        
        Args:
            query_text: The query text to analyze
            
        Returns:
            The detected category or None if uncertain
        """
        # Simple keyword-based detection
        query_lower = query_text.lower()
        
        if any(keyword in query_lower for keyword in ["prove", "proof", "theorem", "lemma"]):
            return "theorem"
        
        if any(keyword in query_lower for keyword in ["solve", "find", "calculate", "compute"]):
            return "problem"
        
        if any(keyword in query_lower for keyword in ["explain", "what is", "how does", "concept"]):
            return "concept"
        
        if any(keyword in query_lower for keyword in ["define", "definition", "meaning"]):
            return "definition"
            
        return None
    
    def add_to_queue(self, query_text: str, **kwargs) -> str:
        """
        Process a query and add it to the priority queue.
        
        Args:
            query_text: The raw query text from the user
            **kwargs: Additional parameters for query processing
            
        Returns:
            A unique ID for the queued query
        """
        query = self.process_query(query_text, **kwargs)
        return self.priority_queue.add_query(query)
    
    def get_next_query(self) -> Tuple[str, MathQuery]:
        """
        Get the next query to process from the priority queue.
        
        Returns:
            A tuple of (query_id, query) or (None, None) if the queue is empty
        """
        return self.priority_queue.get_next_query()
        
    def validate_batch_queries(self, queries: List[Dict[str, Any]]) -> List[Tuple[str, MathQuery]]:
        """
        Validate a batch of queries and add them to the priority queue.
        
        Args:
            queries: List of query dictionaries
            
        Returns:
            List of (query_id, validated_query) tuples for successful validations
        """
        validated_queries = []
        
        for query_dict in queries:
            query_text = query_dict.pop("query", None)
            if not query_text:
                continue
                
            try:
                validated_query = self.process_query(query_text, **query_dict)
                query_id = self.priority_queue.add_query(validated_query)
                validated_queries.append((query_id, validated_query))
            except Exception as e:
                # Log the error but continue processing other queries
                print(f"Error validating query '{query_text}': {str(e)}")
                
        return validated_queries 