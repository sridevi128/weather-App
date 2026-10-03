# Weather App

A simple and user-friendly Weather App built using Python and Streamlit.  
The application allows users to search for weather information by city name and displays the current weather details.

## Features

- Search weather by city name
- Displays current temperature
- Displays humidity
- Displays weather condition
- Displays weather information in a simple interface
- User-friendly Streamlit interface
- Handles invalid city names and API errors
- Uses environment variables to protect the API key

## Technologies Used

- Python
- Streamlit
- Weather API
- Requests
- python-dotenv
- Pytest

## Project Structure

```text
weather-App/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   └── weather_service.py
│
├── tests/
│   └── test_weather_service.py
│
├── .env.example
├── .gitignore
├── .python-version
├── README.md
├── requirements.txt
└── weather.py


## OUTPUT

Enter city name: Hyderabad
API key found: True

Weather Details
City: Hyderabad
Temperature: 32.46 °C
Humidity: 50 %


Enter city name: Bangalore
API key found: True

Weather Details
City: Bangalore
Temperature: 28.12 °C
Humidity: 56 %
Weather: scattered clouds


Enter city name: Chennai
API key found: True

Weather Details
City: Chennai
Temperature: 32.89 °C
Humidity: 66 %
Weather: few clouds
