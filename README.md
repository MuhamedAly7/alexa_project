# Alexa Project
Build your own voice-controlled assistant using Python. This project, named 'Alexa,' incorporates speech recognition, text-to-speech conversion, and various APIs to perform tasks like playing music, fetching the weather, searching the web, and more. Customize it to suit your needs and enhance your Python skills in voice interaction and automation."


##Overview

Alixa is a Python-based virtual assistant that uses various libraries to perform tasks such as speech recognition, text-to-speech conversion, and interaction with external APIs. It is designed to handle voice commands, play music, provide weather updates, fetch information from Wikipedia, perform translations, and more.

##Features

- **Speech Recognition: Alixa utilizes the speech_recognition library to listen for voice commands.

- **Text-to-Speech Conversion: The project supports two text-to-speech libraries, namely pyttsx3 and gTTS, giving users the flexibility to choose their preferred library.

- **Command Handling: Alixa catches voice commands, processes them, and responds accordingly.

- **Multilingual Support: The translation feature allows users to translate text into various languages using the googletrans library.

- **Web Interaction: Alixa can perform web-related tasks such as searching on Google and opening location maps.

- **Weather Updates: The assistant can fetch and announce weather details for a specified city using the OpenWeatherMap API.

- **Prayer Time Reminders: Alixa reminds users of prayer times using the Aladhan API.

- **Calendar and Calculator Integration: The project can open the system's calendar and calculator applications.

- **System Control: Users can instruct Alixa to shut down the device.

##Getting Started

1. Install the required libraries:

```bash

pip install SpeechRecognition gtts playsound pywhatkit wikipedia webbrowser requests pyttsx3 googletrans==4.0.0-rc1

  Set up the Aladhan API key by visiting Aladhan API.

    Run the Alexa.py script.

Usage

    To initiate a conversation with Alixa, say "Alexa."

    Sample Commands:
        "Play [song name]"
        "What's the time?"
        "Speak about [topic]"
        "Search [query]"
        "Translate [text]"

Configuration

    Adjust the use_pyttsx3 variable to choose between pyttsx3 and gTTS for text-to-speech.

    Customize the Aladhan API key in the prayer time reminder section.

    Modify location coordinates for accurate prayer times.

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance Alixa.
