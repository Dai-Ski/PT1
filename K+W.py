from gensim.downloader import load
model = load("glove-wiki-gigaword-50")

# king - man + woman = queen
res = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print(res[0][0]) 

# top 5 similar words
res5 = model.most_similar(positive=['programming'], topn=5)
print(res5)