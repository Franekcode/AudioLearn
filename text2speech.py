from elevenlabs import ElevenLabs, VoiceSettings
from dotenv import load_dotenv
import os
import requests
load_dotenv()
ElevenLabs.api_key = os.getenv("ELEVENLABS_API_KEY")
def text2speech(text):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/gUABw7pXQjhjt0kNFBTF"

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": ElevenLabs.api_key
    }

    data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5,
        "speed": 1.0,
    }
    }

    response = requests.post(url, json=data, headers=headers)
    
    return response




