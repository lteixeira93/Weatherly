import requests


def fetch_weather(city):
    API_KEY = 'TOKEN'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'weather_description': data['weather'][0]['description']
        }
    else:
        return None

print(fetch_weather("Eindhoven"))