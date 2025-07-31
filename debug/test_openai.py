from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../keys.env')

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


file = client.files.create(
    file=open("./LectureNotes.pdf", "rb"),
    purpose="user_data"
)


# Test message
test_input = "How would I declare a variable for a last name?"

# Create messages
messages = [
    {
        "role": "system",
        "content": "You are a cybersecurity tutor. Provide clear, accurate, and engaging explanations about cybersecurity concepts. Focus on practical examples and best practices."
    },
    {
        "role": "user",
        "content": [
                {
                    "type": "file",
                    "file": {
                        "file_id": file.id,
                    }
                },
                {
                    "type": "text",
                    "text": test_input,
                },
            ]
    }
]

try:
    print("Sending request to OpenAI...")
    print("Using API key:", os.getenv('OPENAI_API_KEY')[:6] + "..." if os.getenv('OPENAI_API_KEY') else "No API key found!")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    print("\nResponse received!")
    print("-" * 50)
    print("Output:", response.choices[0].message.content)
except Exception as e:
    print("Error occurred:", str(e)) 