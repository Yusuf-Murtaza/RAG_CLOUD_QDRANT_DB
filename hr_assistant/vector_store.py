"""Step 4. Store chunk embeddings in a vector database FAISS for efficient retrieval."""

import os
from langchain_qdrant import Qdrant, QdrantVectorStore
from qdrant_client import QdrantClient
from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def build_vector_store(chunks):
    """Embed every chunks and upload it into Qdrant cloud collection"""
    logger.info(
        "Embedding %d chunks and uploading to Qdrant cloud collection..." % len(chunks),
        config.QDRANT_COLLECTION_NAME
    )
    embeddings_model = get_embeddings_model()
    vector_store = QdrantVectorStore.from_documents(
        chunks, 
        embedding = embeddings_model,
        url = config.QDRANT_URL,
        api_key = config.QDRANT_API_KEY,
        collection_name = config.QDRANT_COLLECTION_NAME
        )
    logger.info("Uploaded to Qdrant collection %s" % config.QDRANT_COLLECTION_NAME)
    return vector_store


def load_vector_store():
    """Connect to Qdrant cloud collection that was already buit before"""
    logger.info("Connecting to Qdrant cloud")
    embeddings_model = get_embeddings_model()
    
    return QdrantVectorStore.from_documents(
        embedding = embeddings_model,
        url = config.QDRANT_URL,
        api_key = config.QDRANT_API_KEY,
        collection_name = config.QDRANT_COLLECTION_NAME
        )

def vector_store_exists() -> bool:
    """Check if the Qdrant store already exists.
        If the Qdrant collection exists, it means the vector store has
          been built before and we can load it instead of building it again.
    """
    client = QdrantClient(
        url=config.QDRANT_URL,
        api_key=config.QDRANT_API_KEY
        )
    return client.collection_exists(config.QDRANT_COLLECTION_NAME)


def get_retriever(vectorstore, k: int = config.TOP_K_RESULTS):
    """Turn a vectorstore into a retriever that returns the top k most similar chunks for a given query."""
    logger.info(f"Creating retriever from vectorstore with top k results: {k}")
    return vectorstore.as_retriever(search_kwargs={"k": k})

