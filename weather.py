#f866071204a94a17a4b53358251106
import requests
from mood_logic import get_mood_suggestion
API_KEY = "f866071204a94a17a4b53358251106" 

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return None, None

    condition = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    return condition, temp

def main():
    city = input("Enter your city: ")
    condition, temp = get_weather(city)
    if condition:
        suggestion = get_mood_suggestion(condition,city)
        print(f"\nWeather in {city}: {condition}, {temp}°C")
        print(f"Mood Suggestion ➤ {suggestion}")
    else:
        print("City not found. Check spelling and try again.")

if __name__ == "__main__":
    main()


