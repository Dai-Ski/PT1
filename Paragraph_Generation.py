from gensim.downloader import load
import random
model = load("glove-wiki-gigaword-50")
seed_word = "hacking"
sim_words = [w for w, s in model.most_similar(seed_word, topn=5)]
random.shuffle(sim_words)
paragraph = f"The topic of {seed_word} is fascinating, often linked to " + ", ".join(sim_words) + "."
print(paragraph)
