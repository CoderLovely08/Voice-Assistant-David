import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable



# Input text
text = "What is 2 plus 2"

# Send the request and get the response
response_data = send_request(text)
print(response_data)
