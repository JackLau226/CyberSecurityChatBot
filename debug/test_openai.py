from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('keys.env')

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Test message
test_input = "How would I declare a variable for a last name?"

# Create the messages array
messages = [
    {
        "role": "system",
        "content": "You are a cybersecurity tutor. Provide clear, accurate, and engaging explanations about cybersecurity concepts. Focus on practical examples and best practices."
    },
    {
        "role": "user",
        "content": test_input
    }
]

try:
    print("Sending request to OpenAI...")
    print("Using API key:", os.getenv('OPENAI_API_KEY')[:6] + "..." if os.getenv('OPENAI_API_KEY') else "No API key found!")
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    print("\nResponse received!")
    print("-" * 50)
    print("Output:", response.choices[0].message.content)
except Exception as e:
    print("Error occurred:", str(e)) 