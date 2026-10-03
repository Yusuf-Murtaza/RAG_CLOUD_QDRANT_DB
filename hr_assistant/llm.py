"""Step 6. Connect to the LLM (The brain of assistant)"""

from langchain_openrouter import ChatOpenRouter
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_llm():
    """Return the OpenRouter LLM model. Reads OPENROUTER_API_KEY from environment variables."""
    logger.info(f"Loading LLM model: {config.LLM_MODEL_NAME}")
    return ChatOpenRouter(
        model_name=config.LLM_MODEL_NAME, 
        max_tokens=2048,
        temperature=0
        )

