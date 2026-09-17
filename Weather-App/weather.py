import requests
import os
from dotenv import load_dotenv

load_dotenv()

city = input("Enter city name: ")

api_key = os.getenv("OPENWEATHER_API_KEY")
print("API key found:", api_key is not None)


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\nWeather Details")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", weather)
else:
    print("Error: ", response.status_code)
    print(data)