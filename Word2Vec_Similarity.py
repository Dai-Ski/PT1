from gensim.models import Word2Vec
import matplotlib.pyplot as plt

corpus = ["The patient was diagnosed with diabetes.", "Symptoms include fever."]
tokenized = [s.lower().split() for s in corpus]

# Train Model
model = Word2Vec(sentences=tokenized, vector_size=5, window=2, min_count=1, epochs=5)
# Find similar
word = input("Enter word: ").lower()
if word in model.wv:
    print(model.wv.most_similar(word, topn=5))
    
    