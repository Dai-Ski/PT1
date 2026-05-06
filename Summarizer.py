from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = "Generative AI is a type of artificial intelligence system capable of generating text, images, or other media in response to prompts. Generative AI models learn the patterns and structure of their input training data and then generate new data that has similar characteristics. Recent breakthroughs in the field, such as Large Language Models (LLMs) like GPT-4 and Diffusion models like Stable Diffusion, have significantly expanded the capabilities of Generative AI, enabling it to perform tasks like creative writing, coding, and artistic creation with remarkable human-like quality."

inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs["input_ids"], max_length=50, min_length=30, do_sample=False)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(summary)