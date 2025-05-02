from utis import speak
import requests
def get_weather(city):
    API_KEY = "6f1ae5a0a442dc6a2e75fe987c3c576d"  # Replace with your actual OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(base_url).json()
    if response.get('main'):
        temp = response['main']['temp']
        weather_desc = response['weather'][0]['description']
        speak(f"The temperature in {city} is {temp - 273.15:.2f} degrees Celsius with {weather_desc}.")
    else:
        speak(f"Sorry, I couldn't get the weather for {city}.")