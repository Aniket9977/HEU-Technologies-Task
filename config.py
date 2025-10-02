import os

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Models
EMBED_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"

# Retrieval
RETRIEVE_K = 3
SIMILARITY_THRESHOLD = 0.70
