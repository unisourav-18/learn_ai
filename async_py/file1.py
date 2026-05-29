import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAacRd-K0flnQmTKI5i2S632dEJktAZxH0")

# Load model
model = genai.GenerativeModel("gemini-3.5-flash")

# Generate response
response = model.generate_content(
    "National Animal of India?"
)

# Print output
print(response.text)