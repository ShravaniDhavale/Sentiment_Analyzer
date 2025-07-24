from transformers import pipeline

# Load the pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],          # POSITIVE or NEGATIVE
        "score": round(result["score"], 4) # Confidence score
    }
