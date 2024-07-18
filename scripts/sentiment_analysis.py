from textblob import TextBlob

# Load text (use the same text loading method as before)
with open('data/the_spirits_book.txt', 'r') as file:
    text = file.read()

# Perform sentiment analysis
blob = TextBlob(text)
sentiment = blob.sentiment

print(f"Sentiment Analysis:\nPolarity: {sentiment.polarity}\nSubjectivity: {sentiment.subjectivity}")
