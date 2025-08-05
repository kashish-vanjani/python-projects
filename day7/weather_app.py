import requests

API_KEY = "YOUR_API_KEY"  # replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY or API_KEY == "YOUR_API_KEY":
        print("Please get a free API key from OpenWeatherMap and put it in the script.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius; use "imperial" for Fahrenheit
    }

    try:
        resp = requests.get(BASE_URL, params=params, timeout=5)
        data = resp.json()

        if resp.status_code != 200:
            msg = data.get("message", "Could not fetch weather.")
            print(f"Error: {msg.capitalize()}")
            return

        name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {name}, {country}:")
        print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"Condition: {desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.RequestException:
        print("Network error. Please check your connection.")

def main():
    print("Simple Weather CLI App")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        if city:
            get_weather(city)
        else:
            print("Please enter a city name.")

if __name__ == "__main__":
    main()
