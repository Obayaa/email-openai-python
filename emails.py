from simplegmail import Gmail
from simplegmail.query import construct_query
import os

# Setup Gmail connection
gmail = Gmail()

# Construct safe query
query_params = {
    "newer_than": (1, "month")
}

messages = gmail.get_sent_messages(query=construct_query(query_params))


# Parse and score emails
for message in messages:
    plain_text = message.plain if message.plain else message.snippet
    # email_score = score_email(plain_text)

    print("=" * 50)
    print(f"To: {message.recipient}")
    print(f"From: {message.sender}")
    print(f"Subject: {message.subject}")
    print(f"Date: {message.date}")
    # print(f"Score: {email_score}")
    print(f"Snippet: {message.snippet}")


