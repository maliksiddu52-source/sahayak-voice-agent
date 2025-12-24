"""
Speech-to-Text (STT) Module.
Uses SpeechRecognition implementation with Google API.
"""
import speech_recognition as sr

def listen(lang: str = "te-IN"):
    """
    Listen to microphone input and convert to text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (Speak now)")
        # r.adjust_for_ambient_noise(source) # Optional: Adjust for background noise
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing audio...")
            # specific language code for Hindi India: hi-IN
            text = r.recognize_google(audio, language=lang)
            print(f"[Heard]: {text}")
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"STT Service Error: {e}")
            return None
