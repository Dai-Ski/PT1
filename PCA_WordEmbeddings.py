import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.downloader import load
model = load("glove-wiki-gigaword-50")
words = ['football', 'basketball', 'soccer', 'tennis', 'cricket']
vecs = PCA(2).fit_transform([model[w] for w in words])
for i, w in enumerate(words):
    plt.scatter(vecs[i,0], vecs[i,1])
    plt.text(vecs[i,0], vecs[i,1], w)
plt.show()
