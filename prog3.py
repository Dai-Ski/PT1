from gensim.models import Word2Vec # Fixed typo from Nord2Vec [cite: 20]
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Domain-specific corpus [cite: 23-33]
corpus = [
    "The patient was diagnosed with diabetes and hypertension.",
    "MRI scans reveal abnormalities in the brain tissue.",
    "The treatment involves antibiotics and regular monitoring.",
    "Symptoms include fever, fatigue, and muscle pain.",
    "The vaccine is effective against several viral infections.",
    "Doctors recommend physical therapy for recovery.",
    "The clinical trial results were published in a journal.",
    "The surgeon performed a minimally invasive procedure.",
    "The prescription includes pain relievers and anti-inflammatory drugs.",
    "The diagnosis confirmed a rare genetic disorder."
]

# Preprocessing: Tokenization and lowering [cite: 34-36]
tokenized_corpus = [sentence.lower().split() for sentence in corpus]

# Training the model [cite: 35-41]
model = Word2Vec(sentences=tokenized_corpus, vector_size=5, window=2, min_count=1, epochs=5)

# Similarity Search [cite: 42-49]
word = input("Enter a word from the corpus (e.g., patient): ").lower()
if word in model.wv: # Fixed typo from model.ww [cite: 43]
    similar = model.wv.most_similar(word, topn=5)
    print(f"Words similar to '{word}':")
    for i, (w, score) in enumerate(similar, 1):
        print(f"{i}. {w} (Similarity: {score:.4f})")
else:
    print("Word not found in vocabulary.")

# PCA Visualization [cite: 50-62]
words = list(model.wv.index_to_key)
word_vectors = model.wv[words]
pca = PCA(n_components=2)
result = pca.fit_transform(word_vectors)

plt.figure(figsize=(10, 8))
plt.scatter(result[:, 0], result[:, 1])
for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]))
plt.title("Word Embeddings (PCA Projection)")
plt.show()