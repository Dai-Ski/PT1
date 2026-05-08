from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = input("Enter text to summarize: ")
if len(text.split()) > 30:
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=50, min_length=30, do_sample=False)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print(summary)
else:
    print("Please enter more than 30 words for summarization.")
