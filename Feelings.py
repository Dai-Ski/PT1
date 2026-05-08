from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love using Generative AI for my lab work!")
print(result)