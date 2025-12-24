"""
Audio Interface.
Exposes simple functions for the main loop.
"""
from src.voice.stt import listen
from src.voice.tts import speak

def get_audio_input():
    return listen(lang="te-IN")

def play_audio_output(text: str):
    # Detect language roughly or default to Telugu
    # For now, we default to 'te' as per requirements
    speak(text, lang='te')
