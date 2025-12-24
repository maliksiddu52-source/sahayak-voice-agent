"""
Text-to-Speech (TTS) Module.
Uses gTTS (Google Text-to-Speech) for Hindi support.
"""
import os
from gtts import gTTS
import playsound

def speak(text: str, lang: str = 'te'):
    """
    Convert text to speech and play it.
    """
    try:
        print(f"[Speaker]: {text}")
        tts = gTTS(text=text, lang=lang, slow=False)
        filename = "temp_output.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"Error in TTS: {e}")
