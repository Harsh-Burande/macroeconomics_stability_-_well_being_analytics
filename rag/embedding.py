import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
import faiss

def create_index(kb):
    documents = [doc['content'] for doc in kb]

    embeddings = model.encode(documents)

    # Creating FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # add embeddings to the index
    index.add(np.array(embeddings))

    return index