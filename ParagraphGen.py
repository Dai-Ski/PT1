from gensim.downloader import load
import random
model = load("glove-wiki-gigaword-50")

word = "hacking"
sims = [w for w, s in model.most_similar(word, topn=5)]
random.shuffle(sims)

para = f"The topic of {word} is linked to {', '.join(sims)}."
print(para)