from transformers import pipeline
analyzer = pipeline("sentiment-analysis")
result = analyzer("I love using Generative AI for my lab work!")
print(result)
