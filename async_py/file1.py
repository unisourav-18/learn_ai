import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# create client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# generate text
response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    # config=types.GenerateContentConfig(
    #     system_instruction="You are a cat. Your name is Neko."),
    contents="write the preamble of indian constitution"
)

# print output
for chunk in response:
    print(chunk.text, end="")