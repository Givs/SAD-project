import requests


def recommend_materials(weather_info):
    """
    Recomenda materiais de construção com base nas condições climáticas.

    Parâmetros:
    - weather_info: Um dicionário contendo informações sobre temperatura, umidade e velocidade do vento.

    Retorna:
    - Uma lista de materiais recomendados.
    """
    temperature = weather_info['temperature']
    humidity = weather_info['humidity']
    wind_speed = weather_info['wind_speed']

    materials = []

    # Exemplo de regras de decisão
    if temperature > 30:
        materials.append('Isolamento térmico avançado')
    if humidity > 80:
        materials.append('Madeira tratada para alta umidade ou materiais alternativos resistentes à umidade')
    if wind_speed > 50:
        materials.append('Estruturas reforçadas para resistir a ventos fortes')

    if not materials:
        materials.append('Materiais de construção padrão')

    return materials


def get_weather_info(city_name, api_key):
    """
    Obtém informações do tempo para uma cidade específica utilizando a API do OpenWeatherMap.

    Parâmetros:
    - city_name: Nome da cidade
    - api_key: Chave da API do OpenWeatherMap

    Retorna:
    - Um dicionário com informações sobre umidade, temperatura e velocidade do vento em km/h
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
        # Converte a velocidade do vento de m/s para km/h
        wind_speed_kmh = data['wind']['speed'] * 3.6

        weather_info = {
            'humidity': data['main']['humidity'],
            'temperature': data['main']['temp'],
            'wind_speed': wind_speed_kmh
        }

        return weather_info
    else:
        return {'error': 'Failed to retrieve weather information'}

# Substitua 'YOUR_API_KEY' pela sua chave de API real
api_key = 'b70f41432f7ca03f275efffde38b7e96'
city_name = 'Aracaju'

weather_info = get_weather_info(city_name, api_key)
materials_recommended = recommend_materials(weather_info)

print(f"Para a cidade de {city_name}, os seguintes materiais de construção são recomendados:")
for material in materials_recommended:
    print(f"- {material}")

