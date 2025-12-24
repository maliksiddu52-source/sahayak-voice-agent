"""
Main Entry Point.
Run this file to start the Voice Agent.
"""
import time
from src.agent.workflow import Agent
from src.voice.audio import get_audio_input, play_audio_output
from colorama import init, Fore, Style

init()

def main():
    print(Fore.CYAN + "Initializing Sahayak Voice Agent..." + Style.RESET_ALL)
    agent = Agent()
    
    welcome_msg = "నమస్కారం! నేను సహాయక్. నేను మీకు ప్రభుత్వ పథకాల గురించి సహాయం చేయగలను. చెప్పండి, నేను మీకు ఎలా సహాయం చేయగలను?"
    print(Fore.GREEN + f"[Sahayak]: {welcome_msg}" + Style.RESET_ALL)
    play_audio_output(welcome_msg)
    
    while True:
        try:
            print(Fore.YELLOW + "\nListening..." + Style.RESET_ALL)
            user_input = get_audio_input()
            
            if not user_input:
                print(Fore.RED + "No input detected. Trying again..." + Style.RESET_ALL)
                continue
                
            if "exit" in user_input.lower() or "band karo" in user_input.lower() or "aapandi" in user_input.lower():
                goodbye = "Dhanyavadamulu. Malli kaluddam."
                print(Fore.GREEN + f"[Sahayak]: {goodbye}" + Style.RESET_ALL)
                play_audio_output(goodbye)
                break
                
            response = agent.process_input(user_input)
            
            print(Fore.GREEN + f"[Sahayak]: {response}" + Style.RESET_ALL)
            play_audio_output(response)
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
            play_audio_output("Kshaminchandi, edho samasya vachindi.")

if __name__ == "__main__":
    main()
