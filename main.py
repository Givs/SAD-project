from weather_api import get_weather_info
from materials import recommend_materials

api_key = 'b70f41432f7ca03f275efffde38b7e96'  # Substitua pela sua chave de API real
city_name = 'Aracaju'

weather_info = get_weather_info(city_name, api_key)
if 'error' not in weather_info:
    materials_recommended = recommend_materials(weather_info)
    print(f"Para a cidade de {city_name}, os seguintes materiais de construção são recomendados:")
    for material in materials_recommended:
        print(f"- {material}")
else:
    print(weather_info['error'])
