import numpy as np
from rag.embedding import model


# 1. Keyword scoring (for hybrid retrieval)
def keyword_score(query, doc):
    score = 0
    for word in query.lower().split():
        if word in doc["content"].lower() or word in doc.get("tags", []):
            score += 1
    return score


# 2. Hybrid retriever (semantic + keyword)
def hybrid_retriever(query, kb, index, k=3):
    # Convert query to embedding (must be 2D for FAISS)
    query_embedding = model.encode([query])

    # FAISS search
    D, I = index.search(np.array(query_embedding), k)

    # Map indices → documents
    candidates = [kb[i] for i in I[0]]

    # Rerank using keyword score
    ranked = sorted(
        candidates,
        key=lambda doc: keyword_score(query, doc),
        reverse=True
    )

    return ranked[:k]


# 3. Query type filtering
def filter_by_query_type(query, docs):
    query = query.lower()

    if "why" in query or "explain" in query:
        return [d for d in docs if d["type"] == "insight"]

    if "summary" in query:
        return [d for d in docs if d["type"] == "summary"]

    if "model" in query or "prediction" in query:
        return [d for d in docs if "model" in d["type"]]

    return docs


# 4. Final context builder
def retrieve_context(query, kb, index):
    docs = hybrid_retriever(query, kb, index, k=2)
    docs = filter_by_query_type(query, docs)

    context = "\n\n".join([doc["content"] for doc in docs])
    return context