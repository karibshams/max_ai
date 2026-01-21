import os
import requests
from dotenv import load_dotenv
import tempfile
import pygame

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_IDS = {
    "anne": os.getenv("VOICE_ID_ANNE"),
    "maya": os.getenv("VOICE_ID_MAYA"),
    "malik": os.getenv("VOICE_ID_MALIK"),
    "hiro": os.getenv("VOICE_ID_HIRO")
}

VOICE_STYLES = {
    "friendly": {
        "stability": 0.5,
        "similarity_boost": 0.75,
        "style": 0.2,
        "speed": 1.0,
        "description": "Warm, approachable tone"
    },
    "energetic": {
        "stability": 0.3,
        "similarity_boost": 0.7,
        "style": 0.6,
        "speed": 1.15,
        "description": "Excited, dynamic tone"
    },
    "wise": {
        "stability": 0.75,
        "similarity_boost": 0.85,
        "style": 0.05,
        "speed": 0.80,
        "description": "Calm, thoughtful tone"
    }
}

class ElevenLabsTTS:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"
    
    def generate_speech(self, text, voice_id, voice_style):
        url = f"{self.base_url}/text-to-speech/{voice_id}"
        headers = {"xi-api-key": self.api_key}
        
        style_settings = VOICE_STYLES[voice_style]
        
        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": style_settings["stability"],
                "similarity_boost": style_settings["similarity_boost"],
                "style": style_settings["style"],
                "speed": style_settings["speed"]
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

def test_voice(avatar_name, voice_style, text, tts_client):
    if avatar_name.lower() not in VOICE_IDS:
        print(f"❌ Avatar '{avatar_name}' not found. Available: {list(VOICE_IDS.keys())}")
        return
    
    if voice_style.lower() not in VOICE_STYLES:
        print(f"❌ Style '{voice_style}' not found. Available: {list(VOICE_STYLES.keys())}")
        return
    
    voice_id = VOICE_IDS[avatar_name.lower()]
    style_info = VOICE_STYLES[voice_style.lower()]
    
    print(f"\n🎤 {avatar_name.upper()} [{voice_style.upper()}] - {style_info['description']}")
    print(f"   Settings: Stability {style_info['stability']}, Style {style_info['style']}, Speed {style_info['speed']}")
    print(f"   Speaking...")
    
    try:
        audio = tts_client.generate_speech(text, voice_id, voice_style.lower())
        tts_client.play_audio(audio)
        print(f"✅ Finished\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def main():
    if not API_KEY:
        print("❌ ELEVENLABS_API_KEY not found in .env")
        return
    
    tts_client = ElevenLabsTTS(API_KEY)
    
    print("=" * 60)
    print("🎙️  ElevenLabs TTS - Avatar Voice Styles Tester")
    print("=" * 60)
    print(f"Available avatars: {', '.join([k.upper() for k in VOICE_IDS.keys()])}")
    print(f"Available styles: {', '.join([k.upper() for k in VOICE_STYLES.keys()])}\n")
    
    while True:
        print("Select avatar:")
        for i, name in enumerate(VOICE_IDS.keys(), 1):
            print(f"  {i}. {name.upper()}")
        print("  5. Exit")
        
        avatar_choice = input("\nEnter avatar (1-5): ").strip()
        
        if avatar_choice == "5":
            print("👋 Goodbye!")
            break
        
        avatar_map = {"1": "anne", "2": "maya", "3": "malik", "4": "hiro"}
        avatar = avatar_map.get(avatar_choice)
        
        if not avatar:
            print("❌ Invalid choice\n")
            continue
        
        print("\nSelect voice style:")
        for i, style in enumerate(VOICE_STYLES.keys(), 1):
            desc = VOICE_STYLES[style]["description"]
            print(f"  {i}. {style.upper()} - {desc}")
        
        style_choice = input("\nEnter style (1-3): ").strip()
        
        style_map = {"1": "friendly", "2": "energetic", "3": "wise"}
        style = style_map.get(style_choice)
        
        if not style:
            print("❌ Invalid choice\n")
            continue
        
        text = input("\nEnter text to speak: ").strip()
        
        if text:
            test_voice(avatar, style, text, tts_client)
        else:
            print("❌ Text cannot be empty\n")

if __name__ == "__main__":
    main()