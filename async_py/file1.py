import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# create client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# generate text
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="National Animal of India?"
)

# print output
print(response.text)