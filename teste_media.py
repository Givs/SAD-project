import json
import requests
import pandas as pd

API_KEY = 'b70f41432f7ca03f275efffde38b7e96'

def obter_dados_clima(cidade):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro ao obter os dados para a cidade {cidade}: {response.text}')
        return None
        
# Inicializar variáveis de acumulação
total_temp = 0
total_humidity = 0
total_wind_speed = 0

cidades = ['Aracaju, BR', 'Nossa Senhora do Socorro, BR']


# Iterar sobre cada previsão
for cidade in cidades:
    dados = obter_dados_clima(cidade)
    if dados:
        for forecast in dados['list']:
            total_temp += forecast['main']['temp']
            total_humidity += forecast['main']['humidity']
            total_wind_speed += forecast['wind']['speed']


num_forecasts = len(dados['list'])
# Calcular as médias
avg_temp = total_temp / num_forecasts
avg_humidity = total_humidity / num_forecasts
avg_wind_speed = total_wind_speed / num_forecasts

print(num_forecasts)
print("Média de temperatura:", avg_temp)
print("Média de umidade:", avg_humidity)
print("Média de velocidade do vento:", avg_wind_speed)
