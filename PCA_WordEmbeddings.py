import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.downloader import load

print("Loading GloVe model...")
model = load("glove-wiki-gigaword-50")

words = ['football', 'basketball', 'soccer', 'tennis', 'cricket']
embeddings = [model[word] for word in words]

reduced = PCA(n_components=2).fit_transform(embeddings)

plt.figure(figsize=(8, 6))
for i, word in enumerate(words):
    plt.scatter(reduced[i, 0], reduced[i, 1])
    plt.text(reduced[i, 0] + 0.02, reduced[i, 1] + 0.02, word)

plt.title("PCA Visualization of Word Embeddings")
plt.grid(True)
plt.show()

