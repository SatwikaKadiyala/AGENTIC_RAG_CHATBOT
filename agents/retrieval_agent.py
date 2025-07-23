# agents/retrieval_agent.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrievalAgent:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.chunk_store = []

    def _embed(self, texts):
        return self.model.encode(texts)

    def retrieve(self, query, chunks, top_k=5):
        self.chunk_store = chunks
        embeddings = self._embed(chunks)
        self.index.reset()
        self.index.add(np.array(embeddings))

        query_vector = self._embed([query])
        D, I = self.index.search(np.array(query_vector), top_k)

        top_chunks = [chunks[i] for i in I[0] if i < len(chunks)]
        return top_chunks
