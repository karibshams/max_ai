import os
import requests
from dotenv import load_dotenv
import tempfile
import platform
import subprocess
import pygame

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_IDS = {
    "anne": os.getenv("VOICE_ID_ANNE"),
    "maya": os.getenv("VOICE_ID_MAYA"),
    "malik": os.getenv("VOICE_ID_MALIK"),
    "hiro": os.getenv("VOICE_ID_HIRO")
}

class ElevenLabsTTS:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"
    
    def generate_speech(self, text, voice_id):
        url = f"{self.base_url}/text-to-speech/{voice_id}"
        headers = {"xi-api-key": self.api_key}
        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    
    def play_audio(self, audio_data):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp.write(audio_data)
            tmp_path = tmp.name
        
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(tmp_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.delay(100)
        finally:
            os.unlink(tmp_path)

def test_voice(avatar_name, text, tts_client):
    if avatar_name.lower() not in VOICE_IDS:
        print(f"❌ Avatar '{avatar_name}' not found. Available: {list(VOICE_IDS.keys())}")
        return
    
    voice_id = VOICE_IDS[avatar_name.lower()]
    print(f"🎤 {avatar_name.upper()} is speaking...")
    
    try:
        audio = tts_client.generate_speech(text, voice_id)
        tts_client.play_audio(audio)
        print(f"✅ {avatar_name.upper()} finished speaking\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def main():
    if not API_KEY:
        print("❌ ELEVENLABS_API_KEY not found in .env")
        return
    
    tts_client = ElevenLabsTTS(API_KEY)
    
    print("=" * 50)
    print("🎙️  ElevenLabs TTS Avatar Tester")
    print("=" * 50)
    print(f"Available avatars: {', '.join([k.upper() for k in VOICE_IDS.keys()])}\n")
    
    while True:
        print("Select avatar:")
        for i, name in enumerate(VOICE_IDS.keys(), 1):
            print(f"  {i}. {name.upper()}")
        print("  5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "5":
            print("👋 Goodbye!")
            break
        
        avatar_choice = {
            "1": "anne",
            "2": "maya",
            "3": "malik",
            "4": "hiro"
        }.get(choice)
        
        if not avatar_choice:
            print("❌ Invalid choice\n")
            continue
        
        text = input("\nEnter text to speak: ").strip()
        if text:
            test_voice(avatar_choice, text, tts_client)
        else:
            print("❌ Text cannot be empty\n")

if __name__ == "__main__":
    main()