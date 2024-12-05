import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API")
print(API_KEY)

def get_weather(city: str = "Lviv"):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    resp = requests.get(url).json()

    current_weather = {
        "city": city,
        "temp": resp.get("current", {}).get("temp_c"),
        "text": resp.get("current", {}).get("condition", {}).get("text"),
        "icon": resp.get("current", {}).get("condition", {}).get("icon")
    }
    return current_weather

print(get_weather())