from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = input("Enter text (>30 words): ")
if len(text.split()) > 30:
    print(summarizer(text, max_length=50, min_length=30, do_sample=False)[0]['summary_text'])
else:
    print("Please enter more than 30 words.")
