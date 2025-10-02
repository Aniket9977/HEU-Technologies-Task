import numpy as np
from retriever.utils import embed_texts, cosine_sim

class SimpleVectorStore:
    def __init__(self):
        self.docs = []
        self.embeddings = None

    def add_docs(self, docs):
        self.docs.extend(docs)

    def build_index(self):
        texts = [d["text"] for d in self.docs]
        if not texts:
            self.embeddings = np.zeros((0, 1))
            return
        embs = embed_texts(texts)
        self.embeddings = np.array(embs)

    def search(self, query, k=3):
        if self.embeddings is None or self.embeddings.shape[0] == 0:
            return []
        q_emb = np.array(embed_texts([query]))[0]
        sims = [cosine_sim(q_emb, doc_emb) for doc_emb in self.embeddings]
        idx_sorted = np.argsort(sims)[::-1][:k]
        results = []
        for idx in idx_sorted:
            results.append({
                "doc": self.docs[idx],
                "score": sims[idx]
            })
        return results
