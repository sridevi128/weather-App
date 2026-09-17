import os
from dotenv import load_dotenv
from weather_service import WeatherService

def main():
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        print("API key not found. Please set the OPENWEATHER_API_KEY in your environment.")
        return

    city = input("Enter city name: ")
    weather_service = WeatherService(api_key)
    weather_data = weather_service.get_weather(city)

    if weather_data:
        print("\nWeather Details")
        print("City:", city)
        print("Temperature:", weather_data['temperature'], "°C")
        print("Humidity:", weather_data['humidity'], "%")
        print("Weather:", weather_data['description'])
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    main()