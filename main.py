from weather_api import get_weather_info
from materials import recomendar_materiais_construcao
import json

api_key = 'b70f41432f7ca03f275efffde38b7e96'
city_name = 'Aracaju'

weather_info = get_weather_info(city_name, api_key)
if 'error' not in weather_info:
    materials_recommended = recomendar_materiais_construcao(weather_info)

    print(
        f">>> Para a cidade de {city_name}, os seguintes materiais de construção são recomendados:")

    print(json.dumps(materials_recommended,
          sort_keys=True, indent=4, ensure_ascii=False))
else:
    print(weather_info['error'])
