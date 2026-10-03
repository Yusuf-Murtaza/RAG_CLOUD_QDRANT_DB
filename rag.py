import os
from dotenv import load_dotenv

load_dotenv()

print("My 1st RAG POC project")

openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")
jina_api_key = os.environ.get("JINA_API_KEY")

print("OpenRouter API Key:", openrouter_api_key)
print("Jina API Key:", jina_api_key)

# print("Environment variables loaded successfully.")

# from langchain_community.embeddings import JinaEmbeddings

# embeddings_model = JinaEmbeddings(
#     model_name="jina-embeddings-v2-base-en"
# )

# print("Embeddings model loaded successfully -> ", embeddings_model.model_name)

