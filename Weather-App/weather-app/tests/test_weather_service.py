import unittest
from unittest.mock import patch
from src.weather_service import WeatherService

class TestWeatherService(unittest.TestCase):

    @patch('src.weather_service.requests.get')
    def test_get_weather_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "main": {"temp": 20, "humidity": 50},
            "weather": [{"description": "clear sky"}]
        }
        
        service = WeatherService()
        weather = service.get_weather("London")
        
        self.assertEqual(weather['temperature'], 20)
        self.assertEqual(weather['humidity'], 50)
        self.assertEqual(weather['description'], "clear sky")

    @patch('src.weather_service.requests.get')
    def test_get_weather_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"message": "city not found"}
        
        service = WeatherService()
        weather = service.get_weather("InvalidCity")
        
        self.assertIsNone(weather)

if __name__ == '__main__':
    unittest.main()