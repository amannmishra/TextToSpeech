import os
import subprocess
import tempfile
from playsound import playsound
import threading
import time


def speak(text: str, voice: str = "en-CA-LiamNeural") -> None:
    try:
        # Create a temporary file to store the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            output_file = tmpfile.name

        # Construct the TTS command to generate speech
        command = f'edge-tts --voice {voice} --text "{text}" --write-media {output_file}'

        # Run the command to generate the speech
        subprocess.run(command, shell=True, check=True)

        # Play the audio in a separate thread
        def play_audio():
            playsound(output_file)
            # After playing, remove the temporary file
            os.remove(output_file)

        threading.Thread(target=play_audio).start()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        while True:
            text = input("Enter text to speak (or 'exit' to quit): ")
            if text.lower() == 'exit':
                break
            speak(text)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
