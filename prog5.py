import gensim.downloader as api
import random

print("Loading pre-trained GloVe model (50 dimensions)...")
model = api.load("glove-wiki-gigaword-50") # [cite: 70]

def create_paragraph(seed_word, similar_words):
    paragraph = f"The topic of {seed_word} is fascinating, often linked to terms like "
    random.shuffle(similar_words)
    paragraph += ", ".join(similar_words) + "."
    return paragraph

seed = input("Enter a seed word: ").lower()
if seed in model:
    # Get top 5 similar words [cite: 70]
    sws = model.most_similar(seed, topn=5)
    words = [word for word, score in sws]
    print("\nGenerated Paragraph:")
    print(create_paragraph(seed, words))
else:
    print("Seed word not found in GloVe vocabulary.")