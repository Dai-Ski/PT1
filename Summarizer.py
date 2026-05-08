from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = input("Enter text to summarize: ")
if len(text.split()) > 30:
    summary = summarizer(text, max_length=50, min_length=30, do_sample=False)
    print(summary[0]['summary_text'])
else:
    print("Please enter more than 30 words for summarization.")