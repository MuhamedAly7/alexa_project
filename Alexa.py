import speech_recognition
from gtts import gTTS
import os
import pyttsx3
from time import ctime
import os
from playsound import playsound
import pywhatkit
import datetime
import wikipedia
import webbrowser
import requests
import time
import subprocess
from googletrans import Translator

# Function to speak using pyttsx3
def speak_pyttsx3(text, lang):
    engine = pyttsx3.init(driverName='espeak')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# Function to speak using gTTS
def speak_gtts(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio = "output.mp3"
    tts.save(audio)
    playsound(os.path.expanduser("~/Documents/Python_tasks/Alixa_project/output.mp3"))
    os.remove(audio)

listener = speech_recognition.Recognizer()

# Set this variable to choose the TTS library
use_pyttsx3 = False

if use_pyttsx3:
    speak_function = speak_pyttsx3
else:
    speak_function = speak_gtts

speak_function("Hi Muhammad", 'en')
speak_function("I am Alexa", 'en')
speak_function("how can i help you today?", 'en')

# to catch command from user
def catch_command():
    try:
        with speech_recognition.Microphone(device_index=None) as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = ''
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa', '')
                print(command)
    except speech_recognition.UnknownValueError:
        #speak_function("Sorry, I couldn't understand what you want.")
        pass
    except speech_recognition.RequestError as e:
        print(f"Speech recognition request failed: {e}")
    return command



def run_alexa():
    command = catch_command()
    print(command)

    # to play 
    if "play" in command:
        song = command.replace('play', '')
        speak_function("playing" + song, 'en')
        pywhatkit.playonyt(song)

    # to get time now
    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak_function("current time is" + time, 'en')

    # to get summary about anything from wikipedia
    if ("speak about" in command) or ("summary" in command):
        info = wikipedia.summary(command, 1)
        speak_function(info, 'en')
        print(info)

    # to get the date today
    if 'date today' in command:
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        speak_function(date, 'en')

    # to search about anything on google
    if "search" in command:
        search = command.replace("search", "")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak_function("done", 'en')

    # To get location
    if "location" in command:
        location = command.replace("location", "")
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)

    # to get the weather in any country
    if "weather" in command:
        url = "http://api.openweathermap.org/data/2.5/weather"
        api_key = "YOUR API KEY FROM OPENWEATHERMAP ACOUNT"
        speak_function("which city you want to know?", 'en')
        my_response_city = catch_command()
        params = {"q": my_response_city, "appid": api_key}

        response = requests.get(url, params=params)
        weather_data = response.json()

        if response.status_code == 200:
            # Weather data is retrieved successfully
            main_weather = weather_data["weather"][0]["main"]
            description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]

            speak_function(f"Weather in {my_response_city}: {main_weather} - {description}", 'en')
            speak_function(f"Temperature: {temperature} Kelvin", 'en')
        else:
            speak_function(f"Error {response.status_code}: {weather_data['message']}", 'en')

    if "translate" in command:
        # Extract the text to translate
        text_to_translate = command.replace("translate", "")
        languages = {"arabic" : "ar", "french" : "fr", "spanish" : "es", "german" : "de", "japanese" : "ja", "korean" : "ko", "russian" : "ru"}
        speak_function("which language you want?", 'en')

        # Specify the target language (you can modify this as needed)
        while True:
            target_language = ""
            while True:
                target_language = catch_command()
                if(len(target_language) != 0):
                    break

            # get translation text
            translated_text = Translator().translate(text_to_translate, dest=languages[target_language]).text

            # tell me the translation
            speak_function("translation is : ", 'en')
            speak_function(translated_text, languages[target_language])

            speak_function("do you need translation in other language?", 'en')
            my_response = ""
            while True:
                my_response = catch_command()
                if len(my_response) != 0:
                    break
            if my_response == "yes":
                speak_function("which language?", 'en')
            elif my_response == "no":
                speak_function("ok no problem", 'en')
                break
    
    # to open calculator
    if "open calculator" in command:
        open_calc_command = "gnome-calculator"
        res = subprocess.run(open_calc_command, shell=True)
        speak_function("done", 'en')

    # to open calendar
    if "open calendar" in command:
        open_calc_command = "gnome-calendar"
        res = subprocess.run(open_calc_command, shell=True)
        speak_function("done", 'en')
    
    # To shutdown the device
    if "shutdown now" in command:
        # we should add this line '<your-username> ALL=(ALL) NOPASSWD: /sbin/poweroff' to 'visudo' file to power off without writing password
        shutdown_command = "sudo /sbin/poweroff"
        # Run the power off command
        result = subprocess.run(shutdown_command, shell=True)

        # Check the result
        if result.returncode == 0:
            speak_function("System is powering off...")
        else:
            speak_function("Error occurred while trying to power off.")
            speak_function("Error code:", result.returncode)


call_times = 0 # to make alexa remind me specific number of times

while True:
    # Set your location coordinates (latitude, longitude)
    latitude = 29.9
    longitude = 31.25

    # Set the date for which you want to get prayer times (today)
    today = datetime.datetime.today().date()

    # Get prayer times using Aladhan API
    url = f"https://api.aladhan.com/v1/timings/{today}?latitude={latitude}&longitude={longitude}&method=2"
    response = requests.get(url)
    data = response.json()

    # Extract prayer times
    times = data['data']['timings']

    
    # praying reminder
    if (datetime.datetime.now().strftime("%H:%M")) == times['Fajr']:
        if call_times < 2:
            speak_function("time of adahan el Fajr")
            call_times += 1
        elif call_times >= 2:
            time.sleep(50.0)
            call_times = 0

    if (datetime.datetime.now().strftime("%H:%M")) == times['Dhuhr']:
        if call_times < 2:
            speak_function("time of adahan el Dhuhr")
            call_times += 1
        elif call_times >= 2:
            time.sleep(40.0)
            call_times = 0

    if (datetime.datetime.now().strftime("%H:%M")) == times['Asr']:
        if call_times < 2:
            speak_function("time of adahan el Asr")
            call_times += 1
        elif call_times >= 2:
            time.sleep(40.0)
            call_times = 0

    if (datetime.datetime.now().strftime("%H:%M")) == times['Maghrib']:
        if call_times < 2:
            speak_function("time of adahan el Maghrib")
            call_times += 1
        elif call_times >= 2:
            time.sleep(40.0)
            call_times = 0

    if (datetime.datetime.now().strftime("%H:%M")) == times['Isha']:
        if call_times < 2:
            speak_function("time of adahan el Isha")
            call_times += 1
        elif call_times >= 2:
            time.sleep(40.0)
            call_times = 0

    run_alexa()
