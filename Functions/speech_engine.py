import pyttsx3
from decouple import config
from datetime import datetime

USERNAME = str(config("USER"))
BOTNAME = str(config("BOTNAME"))


engine = pyttsx3.init("sapi5")

# Set Rate
engine.setProperty("rate", 190)

# Set Volume
engine.setProperty("volume", 1.0)

# Set Voice (Female)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # type: ignore


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever is passed to it"""

    engine.say(text)
    engine.runAndWait()


def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour

    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")
