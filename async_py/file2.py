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
chat = client.chats.create(model="gemini-2.5-flash-lite")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)
