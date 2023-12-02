import urllib.parse
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q':  urllib.parse.quote(city),
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print the response content for debugging
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Error fetching weather data.")

def main():
    api_key = '5a8e6a987c91b3766fbf313115e7d55d'  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    
    weather_data = get_weather(api_key, city)

    display_weather(weather_data)

if __name__ == "__main__":
    main()
