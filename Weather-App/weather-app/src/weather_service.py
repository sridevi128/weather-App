class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        url = f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            return {
                "temperature": temperature,
                "humidity": humidity,
                "weather": weather
            }
        else:
            raise Exception(f"Error fetching weather data: {response.status_code}")