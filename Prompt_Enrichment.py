import cohere
import gensim.downloader as api

# Use a placeholder or environment variable for the API key
COHERE_API_KEY = "YOUR_API_KEY" 
co = cohere.Client(COHERE_API_KEY)

print("Loading GloVe model...")
model = api.load("glove-wiki-gigaword-50")

prompt = "write an essay on natural disaster"
words = prompt.split()

new_words = [model.most_similar(w, topn=1)[0][0] if w in model else w for w in words]
enriched_prompt = " ".join(new_words)

print(f"Original Prompt: {prompt}")
print(f"Enriched Prompt: {enriched_prompt}")

try:
    if COHERE_API_KEY != "YOUR_API_KEY":
        response = co.chat(message=enriched_prompt)
        print("\nCohere Response:")
        print(response.text)
    else:
        print("\nWarning: Please replace 'YOUR_API_KEY' with a valid Cohere API key in prog4.py.")
        print("[Mock Mode] Cohere response would appear here if a valid API key was provided.")
except Exception as e:
    print(f"\nError calling Cohere API: {e}")
