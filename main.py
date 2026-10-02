from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

LANGUAGES = {
    "1": {"name": "English", "code": "en"},
    "2": {"name": "Hindi", "code": "hi"},
    "3": {"name": "Malayalam", "code": "ml"},
    "4": {"name": "Kannada", "code": "kn"},
    "5": {"name": "Telugu", "code": "te"},
    "6": {"name": "Tamil", "code": "ta"}
}

while True:
    print("\n=== MULTILINGUAL TRANSLATOR ===")
    for key, value in LANGUAGES.items():
        print(f"{key} - {value['name']}")
    print("Type 'exit' to quit.")
    
    src_choice = input("\nSelect language you will TYPE (1-6): ").strip().lower()
    if src_choice == 'exit': break
    dest_choice = input("Select language to TRANSLATE TO (1-6): ").strip().lower()
    if dest_choice == 'exit': break
        
    if src_choice not in LANGUAGES or dest_choice not in LANGUAGES: continue

    src_lang = LANGUAGES[src_choice]["code"]
    dest_lang = LANGUAGES[dest_choice]["code"]

    user_text = input(f"\nType your message: ").strip()
    if user_text.lower() == 'exit': break

    try:
        translated = translator.translate(user_text, src=src_lang, dest=dest_lang)
        print(f"Translation: {translated.text}")
        tts = gTTS(text=translated.text, lang=dest_lang)
        public_download_path = "/sdcard/Download/translator_output.mp3"
        tts.save(public_download_path)
        print("[SUCCESS] Audio saved to Download folder!")
    except Exception as e:
        print(f"Error: {e}")
      
