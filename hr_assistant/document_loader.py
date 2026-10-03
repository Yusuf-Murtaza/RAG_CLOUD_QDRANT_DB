"""Step 1: Load the documents from the data folder"""

from langchain_community.document_loaders import TextLoader
from hr_assistant import config
from hr_assistant.logger import get_logger

def load_documents(file_path: str = config.DATA_FILE_PATH):
    """Load documents from the specified file path and return them as a list of Langchain Document objects."""
    logger = get_logger(__name__)
    logger.info(f"Loading documents from {file_path}")
    loader = TextLoader(file_path, encoding='utf-8')
    documents = loader.load()
    logger.info(f"Loaded {len(documents)} documents from {file_path}")
    return documents

