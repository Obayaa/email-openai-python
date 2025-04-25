from simplegmail import Gmail
from simplegmail.query import construct_query
from textblob import TextBlob  # For sentiment analysis
import os

# Setup Gmail connection
gmail = Gmail()

# Construct safe query
query_params = {
    "newer_than": (1, "day")
}

messages = gmail.get_sent_messages(query=construct_query(query_params))


# Scoring function
def score_email(content):
    blob = TextBlob(content)
    sentiment = blob.sentiment.polarity  # -1 to 1
    word_count = len(content.split())

    sentiment_score = (sentiment + 1) / 2 * 50  # Normalize to 0–50
    length_score = min(word_count, 200) / 200 * 50  # Max 50 pts for 200+ words

    score = sentiment_score + length_score
    return round(score, 2)



# Parse and score emails
for message in messages:
    plain_text = message.plain if message.plain else message.snippet
    email_score = score_email(plain_text)

    print("=" * 50)
    print(f"To: {message.recipient}")
    print(f"From: {message.sender}")
    print(f"Subject: {message.subject}")
    print(f"Date: {message.date}")
    print(f"Score: {email_score}")
    print(f"Snippet: {message.snippet}")


