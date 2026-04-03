import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config


def find_my_ip():
    ip_address = requests.get("https://api64.ipify.org?format=json").json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def play_on_youtube(video):
    kit.playonyt(video)  # type: ignore


def search_on_google(query):
    kit.search(query)  # type: ignore


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+254{number}", message)  # type: ignore


EMAIL = str(config("EMAIL"))
PASSWORD = str(config("PASSWORD"))


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email["To"] = receiver_address
        email["Subject"] = subject
        email["From"] = EMAIL
        email.set_content(message)

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(f"Email Crash Log: {e}")
        return False


NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news():
    news_headlines = []
    try:
        res = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=ke&apiKey={NEWS_API_KEY}&category=general"
        ).json()

        articles = res["articles"]
        for article in articles:
            news_headlines.append(article["title"])

        return news_headlines[:5]

    except Exception as e:
        print(f"News API Crash Log: {e}")
        return ["Sorry Sir, I could not fetch the news at this time."]


OPEN_WEATHER_APP_ID = str(config("OPEN_WEATHER_APP_ID"))


def get_weather_report(city):
    try:
        res = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_APP_ID}&units=metric"
        ).json()

        weather = res["weather"][0]["main"]
        temperature = res["main"]["temp"]
        feels_like = res["main"]["feels_like"]

        return weather, f"{temperature}℃", f"{feels_like}℃"

    except Exception as e:
        print(f"Weather API Crash Log: {e}")
        return "Error", "Unknown", "Unknown"


TMDB_API_KEY = str(config("TMDB_API_KEY"))


def get_trending_movies():
    try:
        trending_movies = []
        res = requests.get(
            f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}"
        ).json()
        results = res["results"]

        for r in results:
            trending_movies.append(r["original_title"])

        return trending_movies[:5]

    except Exception as e:
        print(f"TMDB API Crash Log: {e}")
        return ["Sorry Sir, I could not fetch the trending movies at this time."]


def get_random_joke():
    headers = {"Accept": "application/json"}
    try:
        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()

        return res["joke"]

    except Exception as e:
        print(f"Joke API Crash Log: {e}")
        return "Sorry Sir, I cannot think of jokes right now."


def get_random_advice():
    try:
        res = requests.get("https://api.adviceslip.com/advice").json()
        return res["slip"]["advice"]

    except Exception as e:
        print(f"Random Advice API Crash Log: {e}")
        return "Sorry Sir, I cannot think of some advice right now."
