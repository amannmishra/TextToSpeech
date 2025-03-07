import requests
from playsound import playsound
import os
from typing import Union

def generate_audio(message: str, voice: str = "Brian"):
    # Correct URL format without extra curly braces
    url: str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    try:
        # Send the request to generate the audio
        result = requests.get(url=url, headers=headers)
        if result.status_code == 200:
            return result.content  # Return the audio content if successful
        else:
            print(f"Error: Unable to generate audio. Status code: {result.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def speak(message: str, voice: str = "Brian", folder: str = "", extension: str = ".mp3") -> Union[None, str]:
    try:
        # Generate the audio content
        result_content = generate_audio(message, voice)

        if result_content:
            # Ensure folder exists if it's provided
            if folder and not os.path.exists(folder):
                os.makedirs(folder)

            # Set file path and save the content
            file_path = os.path.join(folder, f"{voice}{extension}")
            with open(file_path, "wb") as file:
                file.write(result_content)
            print(f"File saved to: {file_path}")

            # Play the audio file
            playsound(file_path)

            # Remove the file after playing
            os.remove(file_path)

            return None
        else:
            return "Failed to generate audio"
    except Exception as e:
        print(f"Error: {e}")
        return str(e)

# Example usage
speak("Hello Aman, I am Aayan", folder="audio_files")  # Specify folder
speak("How are you Aman?", folder="audio_files")  # Specify folder
