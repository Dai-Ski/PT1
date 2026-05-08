import fitz  # PyMuPDF
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

if not os.path.exists("ipc.pdf"):
    print("Creating mock content (using text for embedding)...")
    text = "The Indian Penal Code (IPC) is the official criminal code of India. Section 378 defines theft. The punishment for theft is provided in Section 379."
else:
    text = "".join(p.get_text() for p in fitz.open("ipc.pdf"))

print("Processing text and generating embeddings...")
chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

query = "What is punishment for theft?"
print(f"\nQuery: {query}")

query_vec = model.encode([query])
D, I = index.search(query_vec, k=1)

print("\nResult:")
print(chunks[I[0][0]])
