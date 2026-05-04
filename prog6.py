from transformers import pipeline # [cite: 76]

# Initialize the pipeline [cite: 77]
sentiment_analyzer = pipeline("sentiment-analysis")

print("Sentiment Analysis Tool (Type 'exit' to quit)")
while True:
    user_input = input("\nEnter a sentence: ") # [cite: 80]
    
    if user_input.lower() == "exit": # [cite: 81]
        print("Goodbye!")
        break
        
    if not user_input.strip(): # [cite: 84]
        continue
        
    result = sentiment_analyzer(user_input)[0] # [cite: 86]
    print(f"Label: {result['label']}") # [cite: 87]
    print(f"Confidence: {result['score']:.4f}") # [cite: 88]