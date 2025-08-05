#  Weather CLI App

A simple command-line Python app that fetches and displays real-time weather data using the OpenWeatherMap API.

---

## Features
- Current temperature (in Celsius)  
- "Feels like" temperature  
- Weather condition description (e.g., clear sky, rain)  
- Humidity percentage  
- Wind speed  
- Handles invalid city names and network issues gracefully  

---

## Requirements
- Python 3.x  
- `requests` library  

Install the dependency if you don’t have it:
```bash
pip install requests

 `````
---

## Setup & How to Run

1. Get an API key
Sign up at OpenWeatherMap and get a free API key.

2. Add your API key
Open weather_app.py and locate this line:
```bash
API_KEY = "YOUR_API_KEY"

 `````
Replace "YOUR_API_KEY" with your real key. Example:
```bash
API_KEY = "abcd1234efgh5678ijkl9012mnop3456"

 `````
Run the script:
```bash
python weather_app.py

`````
Enter a city name when prompted to see its current weather.
