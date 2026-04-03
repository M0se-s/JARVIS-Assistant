import speech_recognition as sr
from random import choice
from utils import opening_text
from datetime import datetime
from Functions.speech_engine import speak


def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  # type: ignore
        if "exit" not in query and "stop" not in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 or hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()
    except Exception:
        speak("Sorry, I could not understand. Could you please say that again?")
        query = "None"
    return query
