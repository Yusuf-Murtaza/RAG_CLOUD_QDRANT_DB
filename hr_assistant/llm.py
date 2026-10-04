"""Step 6. Connect to the LLM (The brain of assistant)"""

from hr_assistant.gateway import get_gateway_llm
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_llm():
    """Return the Groq LLM model. Reads GROQ_API_KEY from environment variables."""
    logger.info("Initializing LLM via Portkey....")
    return get_gateway_llm()
