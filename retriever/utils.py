from openai import OpenAI
import numpy as np
import os
from dotenv import load_dotenv
EMBED_MODEL = "text-embedding-3-small"
load_dotenv()
OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def embed_texts(texts, model=EMBED_MODEL):

    resp = client.embeddings.create(
        model=model,
        input=texts
    )
    return [d.embedding for d in resp.data]

def cosine_sim(a, b):
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))
