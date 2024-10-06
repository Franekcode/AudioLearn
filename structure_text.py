from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Get the API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=openai_api_key)

def structure_text(text):
     response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": "You are a helpful teacher trying to explain the following text to a student by talking to him, in a simple way. Always mind that the student is currently doing such activty that he can't fully lean on the phone, like he is running or in a commute or driving, and you are talking to him like he is listening to a podcast."},
            {"role": "user", "content": f"Now, your goal is to convert and explain this text in such way: {text}"}
        ]
    )
     response = response.choices[0].message.content.strip()
    
     return response 