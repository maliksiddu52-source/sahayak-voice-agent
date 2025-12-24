"""
Text-to-Speech (TTS) Module.
Uses edge-tts (Microsoft Edge TTS) for faster and better quality voice.
"""
import os
import subprocess
import playsound

def speak(text: str, lang: str = 'te'):
    """
    Convert text to speech and play it using edge-tts CLI.
    """
    try:
        print(f"[Speaker]: {text}")
        filename = "temp_output.mp3"
        
        voice = "te-IN-ShrutiNeural"
        
        rate = "+20%"
        
        command = [
            "edge-tts",
            "--voice", voice,
            "--rate", rate,
            "--text", text,
            "--write-media", filename
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"EdgeTTS Error: {result.stderr}")
            return

        playsound.playsound(filename)
        os.remove(filename)
        
    except Exception as e:
        print(f"Error in TTS: {e}")
