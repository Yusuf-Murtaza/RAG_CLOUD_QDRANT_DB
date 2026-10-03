"""Step 0b: Langsmith Tracing for Langchain

Lamgmsmith tracing needs no wiring in our own code - Lnagchain looks for LANGSMITH_TRACING , 
LANGSMITH_ENDPOINT, LANGSMITH_API_KEY, LANGSMITH_PROJECT directly in the environment (loaded from .env by config.py) and if 
tracing is turned on, it will automatically enable tracing for all LLM Calls. Tools Calls, Agent Steps to your Langsmith project

This module doesn't turns Tracing on or off, it just checks if tracing is enabled and logs the status. 
So it's obvious from the logs (see logger.py) whether this run was traced"""

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def check_langsmith_tracing() -> None:
    """Log the status of Langsmith tracing whether enabled or not."""
    tracing_on = config.LANGSMITH_TRACING.lower() == 'true'
    if tracing_on and config.LANGSMITH_API_KEY:
        logger.info("Langsmith tracing is enabled - project: %s, traces at: %s", 
                    config.LANGSMITH_PROJECT, 
                    "https://smith.langchain.com"
                    )
    else:
        logger.info("Langsmith tracing is disabled (Set LANGSMITH_TRACING=true and LANGSMITH_API_KEY in .env to enable tracing)")


