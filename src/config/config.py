import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    OUTPUT_DIR = "output"
    CONTEXT_LEARNING_PATH = "data/context_learning"
    MANIM_DOCS_PATH = "data/rag/manim_docs"
    EMBEDDING_MODEL = "azure/text-embedding-3-large"
    OPEN_ROUTER_API_KEY = os.getenv('OPEN_ROUTER_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    # Kokoro TTS configurations
    KOKORO_MODEL_PATH = os.getenv('KOKORO_MODEL_PATH')
    KOKORO_VOICES_PATH = os.getenv('KOKORO_VOICES_PATH')
    KOKORO_DEFAULT_VOICE = os.getenv('KOKORO_DEFAULT_VOICE')
    KOKORO_DEFAULT_SPEED = float(os.getenv('KOKORO_DEFAULT_SPEED', '1.0'))
    KOKORO_DEFAULT_LANG = os.getenv('KOKORO_DEFAULT_LANG') 