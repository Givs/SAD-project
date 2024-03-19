import requests
import pandas as pd

API_KEY = 'b70f41432f7ca03f275efffde38b7e96'

def obter_dados_clima(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro ao obter os dados para a cidade {cidade}: {response.text}')
        return None

def recomendar_materiais_construcao(clima):
    temperatura = clima['main']['temp']
    umidade = clima['main']['humidity']
    velocidade_vento = clima['wind']['speed']
    
    materiais_recomendados = {}
    
    # Tijolos recomendados para diferentes faixas de temperatura
    if temperatura < 10:
        materiais_recomendados['Tijolos'] = "Tijolos de barro cozido"
    elif temperatura >= 10 and temperatura < 25:
        materiais_recomendados['Tijolos'] = "Tijolos de concreto"
    else:
        materiais_recomendados['Tijolos'] = "Tijolos térmicos"
    
    # Cores recomendadas para diferentes faixas de umidade
    if umidade < 50:
        materiais_recomendados['Cor'] = "Cores mais claras para refletir o calor"
    else:
        materiais_recomendados['Cor'] = "Cores mais escuras para absorver o calor"
    
    # Outros materiais recomendados com base na velocidade do vento
    if velocidade_vento >= 10:
        materiais_recomendados['Outros'] = "Concreto reforçado para estruturas mais robustas"
    else:
        materiais_recomendados['Outros'] = "Concreto padrão para estruturas comuns"
    
    return materiais_recomendados

cidades = ['Rio de Janeiro', 'São Paulo', 'Brasília', 'Salvador', 'Fortaleza', 'Aracaju']

dados_clima = []

for cidade in cidades:
    dados = obter_dados_clima(cidade)
    if dados:
        clima = dados
        materiais_recomendados = recomendar_materiais_construcao(clima)
        dados_clima.append({
            'Cidade': cidade,
            'Temperatura (C)': clima['main']['temp'],
            'Umidade (%)': clima['main']['humidity'],
            'Velocidade do Vento (m/s)': clima['wind']['speed'],
            'Tijolos Recomendados': materiais_recomendados['Tijolos'],
            'Cor da Casa Recomendada': materiais_recomendados['Cor'],
            'Outros Materiais Recomendados': materiais_recomendados['Outros']
        })

df = pd.DataFrame(dados_clima)

df.to_csv('recomendacoes_materiais_construcao.csv', index=False)

print("Recomendações de materiais salvos com sucesso em 'recomendacoes_materiais_construcao.csv'.")
