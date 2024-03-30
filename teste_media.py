import json
import requests
import pandas as pd

API_KEY = 'b70f41432f7ca03f275efffde38b7e96'

def obter_dados_clima(cidade):
    url = f"//history.openweathermap.org/data/2.5/aggregated/year?q={cidade},GB&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro ao obter os dados para a cidade {cidade}: {response.text}')
        return None

# Inicializar as variáveis para acumular os valores
soma_temp = 0
soma_umidade = 0
soma_velocidade_vento = 0
total_dias = 0

cidades = ['Rio de Janeiro', 'São Paulo', 'Brasília', 'Salvador', 'Fortaleza', 'Aracaju']

# Iterar sobre os dados de cada dia
for cidade in cidades:
    dados = obter_dados_clima(cidade)
    for dia in dados['result']:
        # Verificar se o dia tem dados de temperatura, umidade e velocidade do vento
        if 'temp' in dia and 'humidity' in dia and 'wind' in dia:
            # Acumular os valores
            soma_temp += dia['temp']['mean']
            soma_umidade += dia['humidity']['mean']
            soma_velocidade_vento += dia['wind']['mean']
            total_dias += 1

# Calcular as médias
media_temp = soma_temp / total_dias
media_umidade = soma_umidade / total_dias
media_velocidade_vento = soma_velocidade_vento / total_dias

# Imprimir as médias
print("Média de temperatura ao longo do ano:", media_temp)
print("Média de umidade ao longo do ano:", media_umidade)
print("Média de velocidade do vento ao longo do ano:", media_velocidade_vento)
