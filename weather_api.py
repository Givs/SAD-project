import requests


def get_weather_info(city_name, api_key):
    """
    Obtém informações do tempo para uma cidade específica utilizando a API do OpenWeatherMap.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Failed to retrieve weather information'}
