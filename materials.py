def recommend_materials(weather_info):
    """
    Recomenda materiais de construção com base nas condições climáticas.
    """
    temperature = weather_info['temperature']
    humidity = weather_info['humidity']
    wind_speed = weather_info['wind_speed']

    materials = []
    if temperature > 30:
        materials.append('Isolamento térmico avançado')
    if humidity > 80:
        materials.append('Madeira tratada para alta umidade ou materiais alternativos resistentes à umidade')
    if wind_speed > 50:
        materials.append('Estruturas reforçadas para resistir a ventos fortes')
    if not materials:
        materials.append('Materiais de construção padrão')
    return materials
