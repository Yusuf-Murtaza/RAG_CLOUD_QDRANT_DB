"""Step 3. Turn text into numbers (Vectors) using Jina"""

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_embeddings_model():
    """Return the Jina embeddings model. Reads JINA_API_KEY from environment variables."""
    logger.info(f"Loading embeddings model: {config.EMBEDDINGS_MODEL_NAME}")
    return JinaEmbeddings(model_name=config.EMBEDDINGS_MODEL_NAME)

