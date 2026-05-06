from transformers import pipeline
analyzer = pipeline("sentiment-analysis")

text = "This lab is actually fire."
result = analyzer(text)[0]
print(f"{result['label']}: {result['score']:.4f}")