"""Allsettings for the HR Assistant project."""

import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables / secrets for API keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
JINA_API_KEY = os.environ.get("JINA_API_KEY")

#GATEWAY
PORTKEY_API_KEY = os.environ.get("PORTKEY_API_KEY")  # Portkey AI API key
PORTKEY_CONFIG_ID = os.environ.get("PORTKEY_CONFIG_ID")

#GUARD MODELS
GUARD_MODEL_NAME = "openai/gpt-oss-safeguard-20b"  # Example guard model name

#TRACING
LANGSMITH_TRACING = os.environ.get("LANGSMITH_TRACING", "false")  # Default to 'false' if not set
LANGSMITH_ENDPOINT = os.environ.get("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.environ.get("LANGSMITH_PROJECT")

#Define path data/ Vectorstore

DATA_FILE_PATH = os.path.join('data', 'hr_policy.txt')

#Vectorstore
#1. In Memory like a=10
#2. Persistent memory like storing in folders. Let say we have 100GB of data which took 10 hours to ingest and create embeddings. 
# If we save it then we can use it again and again.
# if we don't save it then we need to ingest it again
#3. Cloud based vectorstore like Pinecone, Weaviate, Milvus, etc.

QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_COLLECTION_NAME = os.environ.get("QDRANT_COLLECTION_NAME", "hr_policy")  # Default collection name

#MODEL
#LLM & EMBEDDINGS_MODEL_NAME
LLM_MODEL_NAME = "openai/gpt-oss-120b"
EMBEDDINGS_MODEL_NAME = "jina-embeddings-v2-base-en"  # Example embedding model name

#CHUNK / TEXT SPLITTING CONFIG
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

#RETRIEVAL RESULTS
TOP_K_RESULTS = 3  # Number of top results to retrieve

#SYSTEM PROMPT
SYSTEM_PROMPT = """You are an HR assistant. You have access to the company's HR policy documents. 
Your task is to provide accurate and helpful information to employees regarding HR policies, procedures, 
and practices. Do not provide information that is not present in the HR policy documents. 
Do not guess or create anything on your own 
"""

def check_api_keys() -> None:
    """Check if the required API keys are set in the environment variables."""
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set. Please set it in the .env file.")
    if not JINA_API_KEY:
        raise ValueError("JINA_API_KEY is not set. Please set it in the .env file.")
    
