# Weather Application

This is a simple weather application that fetches and displays weather information based on the city provided by the user. The application interacts with the OpenWeather API to retrieve real-time weather data.

## Project Structure

```
weather-app
├── src
│   ├── __init__.py          # Marks the directory as a Python package
│   ├── config.py            # Configuration settings and environment variable loading
│   ├── main.py              # Entry point for the application
│   └── weather_service.py    # Contains the WeatherService class for API interaction
├── tests
│   └── test_weather_service.py # Unit tests for the WeatherService class
├── .env.example              # Template for environment variables
├── .gitignore                # Specifies files to be ignored by Git
├── README.md                 # Documentation for the project
├── requirements.txt          # Lists project dependencies
└── .python-version           # Specifies the Python version for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd weather-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   - Copy `.env.example` to `.env` and add your OpenWeather API key:
     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the prompts to enter the city name and retrieve the weather information.

## Testing

To run the unit tests, use the following command:
```
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.