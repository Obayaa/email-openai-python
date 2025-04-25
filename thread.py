# from simplegmail import Gmail
# from simplegmail.query import construct_query

# # Initialize Gmail connection
# gmail = Gmail()

# # Fetch recent messages with any filter you like
# messages = gmail.get_sent_messages(query="To:doraappiah1975@gmail.com") 

# if messages:
#     # Grab the thread_id from the first message
#     thread_id = messages[0].thread_id
#     print(f"Thread ID: {thread_id}")

#     # Fetch ALL sent messages (or inbox) and filter manually
#     all_messages = gmail.get_sent_messages()  # or gmail.get_messages() for all inbox

#     # Filter by the thread_id
#     thread_messages = [msg for msg in all_messages if msg.thread_id == thread_id]

#     for msg in thread_messages:
#         print("=" * 50)
#         print(f"From: {msg.sender}")
#         print(f"To: {msg.recipient}")
#         print(f"Subject: {msg.subject}")
#         print(f"Date: {msg.date}")
#         print(f"Body: {msg.plain if msg.plain else msg.snippet}")






# This code snippet is using the `simplegmail` library in Python to interact with the Gmail API.
from simplegmail import Gmail
import base64
import re

def strip_quoted_text(body):
    # Strip out common quoted reply patterns
    patterns = [
        r"On\s.+\s+wrote:",          # "On Mar 5, 2025 at 11:56 PM X wrote:"
        r"-----Original Message-----",  # Outlook style
        r"From: .*",                 # Generic "From:" line
        r"Sent: .*",                 # "Sent: date"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, body)
        if match:
            return body[:match.start()].strip()
    return body.strip()



# Initialize Gmail connection
gmail = Gmail()
service = gmail.service  # This gives you access to the underlying Gmail API service

# Get a thread ID from an existing message
messages = gmail.get_sent_messages(query="To: arhinr@gmail.com") 

if messages:
    # Get the thread ID from the first message
    thread_id = messages[0].thread_id
    print(f"Found thread ID: {thread_id}")
    
    # Use the threads.get method directly
    thread = service.users().threads().get(userId='me', id=thread_id).execute()
    
    # Process the thread data
    if 'messages' in thread:
        print(f"Found {len(thread['messages'])} messages in thread")
        for message in thread['messages']:
            # Extract headers
            headers = {header['name']: header['value'] for header in message['payload']['headers']}
            
            print("=" * 50)
            print(f"From: {headers.get('From', 'Unknown')}")
            print(f"To: {headers.get('To', 'Unknown')}")
            print(f"Subject: {headers.get('Subject', 'No Subject')}")
            print(f"Date: {headers.get('Date', 'Unknown')}")
            
            # Extracting message body
            try:
                def extract_body(payload):
                    if 'parts' in payload:
                        for part in payload['parts']:
                            # Nested parts
                            if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                                return base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                            elif 'parts' in part:  # Deeply nested
                                return extract_body(part)
                    elif 'body' in payload and 'data' in payload['body']:
                        return base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')
                    return None


                body = extract_body(message['payload'])
                if body:
                    clean_body = strip_quoted_text(body)
                    print(f"Body: {clean_body[:500]}...\n")
                else:
                    print(f"Snippet: {message.get('snippet', 'No snippet available')}")


            except Exception as e:
                print(f"Error extracting body: {e}")
                print(f"Snippet: {message.get('snippet', 'No snippet available')}")








