"""Step 4. Store chunk embeddings in a vector database FAISS for efficient retrieval."""

import os
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def build_vector_store(chunks):
    """Embed every chunks and build a searchable faiss index in memory"""
    logger.info(f"Building FAISS vectorstore from {len(chunks)} chunks.")
    embeddings_model = get_embeddings_model()
    vector_store = FAISS.from_documents(chunks, embeddings_model)
    logger.info("Built FAISS vectorstore in memory.")
    return vector_store

#Save vectorstore to disk
def save_vector_store(vectorstore, path :str =config.VECTOR_STORE_PATH)-> None:
    """Save the FAISS vectorstore to disk so that it can be loaded later without re-embedding the documents."""
    vectorstore.save_local(path)
    logger.info(f"Saved FAISS vectorstore to {path}")

def load_vector_store(path: str = config.VECTOR_STORE_PATH):
    """Load the FAISS vectorstore from disk."""
    logger.info(f"Loading FAISS vectorstore from {path}")
    embeddings_model = get_embeddings_model()
    #allow_dangerous_deserialization=True is used to allow loading of the vectorstore 
    # even if it was created with a different version of FAISS.
    return FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)

def vector_store_exists(path: str = config.VECTOR_STORE_PATH) -> bool:
    """Check if the FAISS vectorstore exists on disk."""
    return os.path.exists(os.path.join(path, "index.faiss"))

def get_retriever(vectorstore, k: int = config.TOP_K_RESULTS):
    """Turn a vectorstore into a retriever that returns the top k most similar chunks for a given query."""
    logger.info(f"Creating retriever from vectorstore with top k results: {k}")
    return vectorstore.as_retriever(search_kwargs={"k": k})

