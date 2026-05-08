from gensim.downloader import load
model = load("glove-wiki-gigaword-50")
# Analogy: king - man + woman = queen
print(model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1))
# Top 5 similar words
print(model.most_similar(positive=['programming'], topn=5))