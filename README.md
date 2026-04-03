# JARVIS-Assistant

A Python-based voice assistant inspired by “JARVIS”. It listens for voice commands, speaks responses back, and can perform basic **system** actions (open apps/camera) and **online** actions (Wikipedia, YouTube, Google search, news, weather, jokes, advice, email, WhatsApp).

## Features

### System commands
- Open Notepad
- Open Discord (attempts to locate Discord.exe dynamically on Windows)
- Open Calculator
- Open Camera (Windows Camera app)

### Online commands
- Get your public IP address
- Wikipedia search (summary)
- Play videos on YouTube
- Google search
- Send WhatsApp messages
- Send email (SMTP via Gmail)
- Random jokes
- Random advice
- Trending movies (TMDB)
- Latest news (NewsAPI)
- Weather report (OpenWeather)

## Project Structure
- `main.py` — app entrypoint (command loop)
- `Functions/`
  - `speech_engine.py` — text-to-speech + greeting
  - `user_input.py` — microphone input + speech recognition
  - `os_ops.py` — opening apps/camera
  - `online_ops.py` — web APIs (news/weather/movies/jokes/etc.)
- `utils.py` — small shared text snippets

## Requirements
This project uses these Python packages (based on imports in the code):
- `requests`
- `wikipedia`
- `pywhatkit`
- `python-decouple`
- `pyttsx3`
- `SpeechRecognition`

You will also need microphone access.

> Note: `pyttsx3` in this project is initialized with the `sapi5` driver, which is Windows-specific.

## Setup

### 1) Clone the repository
```bash
git clone https://github.com/M0se-s/JARVIS-Assistant.git
cd JARVIS-Assistant
```

### 2) Install dependencies
If you don’t have a `requirements.txt` yet, install manually:
```bash
pip install requests wikipedia pywhatkit python-decouple pyttsx3 SpeechRecognition
```

### 3) Create a `.env` file
This project reads secrets/config using `python-decouple`. Create a file named `.env` in the repo root:

```env
# Used by Functions/speech_engine.py
USER=YourName
BOTNAME=JARVIS

# Used by Functions/online_ops.py (email sending)
EMAIL=your_email@gmail.com
PASSWORD=your_app_password_or_password

# Used by Functions/online_ops.py (APIs)
NEWS_API_KEY=your_newsapi_key
OPEN_WEATHER_APP_ID=your_openweather_key
TMDB_API_KEY=your_tmdb_key
```

**Important:** If you use Gmail, you’ll likely need an **App Password** (recommended) instead of your normal password.

## Run
```bash
python main.py
```

## Example Voice Commands
Try saying things like:
- “open notepad”
- “open discord”
- “open calculator”
- “open camera”
- “ip address”
- “wikipedia”
- “youtube”
- “search google”
- “send whatsapp message”
- “send an email”
- “joke”
- “advice”
- “trending movies”
- “news”
- “weather”
- “exit” / “stop” / “sleep”

## Notes / Limitations
- Some system commands are Windows-focused.
- WhatsApp messaging uses `pywhatkit` and may open a browser session.
- News is currently set to `country=ke` (Kenya) in the NewsAPI request. You can change this in `Functions/online_ops.py`.

## License
No license specified yet. Add a LICENSE file if you want to define usage terms.
