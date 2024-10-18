from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity and subjectivity
    sentiment = blob.sentiment
    
    # Print the sentiment score
    print(f"Sentiment Analysis of the text:\n")
    print(f"Polarity: {sentiment.polarity} (range: -1 to 1)")
    print(f"Subjectivity: {sentiment.subjectivity} (range: 0 to 1)")

    # Interpretation of the results
    if sentiment.polarity > 0:
        print("The text has a positive sentiment.")
    elif sentiment.polarity < 0:
        print("The text has a negative sentiment.")
    else:
        print("The text has a neutral sentiment.")

# Example usage
text = input("Enter text to analyze sentiment: ")
analyze_sentiment(text)
