import requests
import Functions.online_ops as web
import Functions.os_ops as system
from Functions.speech_engine import speak, greet_user
from Functions.user_input import take_user_input


if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input().lower()

        # System Commands
        if "open notepad" in query:
            system.open_app("notepad")

        elif "open discord" in query:
            system.open_app("discord")

        elif "open calculator" in query:
            system.open_app("calculator")

        elif "open camera" in query:
            system.open_camera()

        # Online Commands
        elif "ip address" in query:
            ip = web.find_my_ip()
            speak(f"Your IP address is {ip}.")
            print(f"IP Address: {ip}")

        elif "wikipedia" in query:
            speak("What do you want to search on Wikipedia, Sir?")
            search_query = take_user_input().lower()
            results = web.search_on_wikipedia(search_query)
            speak(f"According to Wikipedia: {results}")
            print(results)

        elif "youtube" in query:
            speak("What do you want to play on Youtube, Sir?")
            video = take_user_input().lower()
            web.play_on_youtube(video)

        elif "search google" in query:
            speak("What do you want to search on Google, Sir?")
            search_query = take_user_input().lower()
            web.search_on_google(search_query)

        elif "send whatsapp message" in query:
            speak(
                "What number should I send the message to? Please enter it in the terminal."
            )
            number = input("Enter the number (+254...): ")
            speak("What is the message?")
            message = take_user_input().lower()
            web.send_whatsapp_message(number, message)
            speak("Message sent.")

        elif "send an email" in query:
            speak(
                "What email address should I send this to? Please enter it in the terminal."
            )
            receiver = input("Enter email address: ")
            speak("What should the subject be?")
            subject = take_user_input().capitalize()
            speak("What is the message?")
            message = take_user_input().capitalize()

            if web.send_email(receiver, subject, message):
                speak("I've sent the email, Sir.")

            else:
                speak(
                    "Something went wrong while sending the mail. Please check the logs."
                )

        elif "joke" in query:
            speak("Hope you like this one")
            joke = web.get_random_joke()
            speak(joke)
            print(joke)

        elif "advice" in query:
            speak("Here is some advice.")
            advice = web.get_random_advice()
            speak(advice)
            print(advice)

        elif "trending movies" in query:
            speak("Here are the trending movies right now.")
            movies = web.get_trending_movies()
            for movie in movies:
                speak(movie)
            print(*movies, sep="\n")

        elif "news" in query:
            speak("Reading the latest headlines.")
            headlines = web.get_latest_news()
            for headline in headlines:
                speak(headline)
            print(*headlines, sep="\n")

        elif "weather" in query:
            try:
                ip_address = web.find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text

            except Exception:
                print("IP location failed. Defaulting to Nairobi.")
                city = "Nairobi"

            speak(f"Getting the weather report for{city}")
            weather, temp, feels = web.get_weather_report(city)

            if weather == "Error":
                speak("Sorry Sir, I could not fetch the weather right now.")

            else:
                speak(f"The current temperature is {temp}, but it feels like {feels}.")
                speak(f"The forecast calls for {weather}.")
                print(f"Weather: {weather} | Temp: {temp} | Feels: {feels}")

        # Shutdown
        elif "exit" in query or "stop" in query or "sleep" in query:
            speak("Shutting down. Goodbye, Sir.")
            break
