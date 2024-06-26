import requests
import pandas as pd
import concurrent.futures

from materials import recomendar_materiais_construcao

API_KEY = 'b70f41432f7ca03f275efffde38b7e96'


def obter_dados_clima(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f'Erro ao obter os dados para a cidade {cidade}: {response.text}')
        return None


def obter_data_clima(cidade):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f'Erro ao obter os dados para a cidade {cidade}: {response.text}')
        return None


def obter_dados_cidade(cidades):
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
                'Telhas Recomendadas': materiais_recomendados['Telhas'],
                'Madeiras Recomendadas': materiais_recomendados['Madeiras'],
                'Metais Recomendados': materiais_recomendados['Metais'],
                'Outros Materiais Recomendados': materiais_recomendados['Outros']
            })

    return dados_clima


if __name__ == '__main__':
    print('>>> Recomendações de materiais de construção para diferentes condições climáticas <<<')

    cidades_raw = ['Aracaju, BR', 'Nossa Senhora do Socorro, BR', 'Lagarto, BR', 'Itabaiana, BR', 'São Cristóvão, BR', 'Estância, BR', 'Nossa Senhora da Glória, BR',
                   'Propriá, BR', 'Itabaianinha, BR', 'Capela, BR', 'Simão Dias, BR', 'Nossa Senhora das Dores, BR', 'Poço Verde, BR', 'Tobias Barreto, BR', 'Umbaúba, BR',
                   'Campo do Brito, BR', 'Boquim, BR', 'Indiaroba, BR', 'Japaratuba, BR', 'Pedrinhas, BR', 'Maruim, BR', 'Siriri, BR', 'Pacatuba, BR',
                   'Rosário do Catete, BR', 'Monte Alegre de Sergipe, BR', 'Brejo Grande, BR', 'Salgado, BR', 'São Miguel do Aleixo, BR', 'Neópolis, BR', 'Areia Branca, BR',
                   'Moita Bonita, BR', 'Itabi, BR', 'Malhador, BR', 'Gararu, BR', 'Arauá, BR', 'Macambira, BR', 'Pedra Mole, BR', 'Cristinápolis, BR', 'Malhada dos Bois, BR',
                   'Nossa Senhora Aparecida, BR', 'Telha, BR', 'Cumbe, BR', 'Feira Nova, BR', 'Pinhão, BR', 'Lagoa Funda, BR', 'Poço Redondo, BR', 'Divina Pastora, BR',
                   'Ilha das Flores, BR', 'Canhoba, BR', 'Santa Rosa de Lima, BR', 'Nossa Senhora de Lourdes, BR', 'Pirambu, BR', 'São Francisco, BR', 'Carira, BR',
                   'Laranjeiras, BR', 'Riachão do Dantas, BR', 'Santa Luzia do Itanhy, BR', 'Porto da Folha, BR', 'Tomar do Geru, BR', 'Aquidabã, BR',
                   'Santana do São Francisco, BR', 'Carmópolis, BR', 'Macambira, BR', 'Canindé de São Francisco, BR', 'Siriri, BR', 'Pedra Branca, BR', 'Gracho Cardoso, BR']

    print(
        f'>>> Obtendo dados climáticos para {len(cidades_raw)} cidades de Sergipe...')

    # Calculate length of each portion
    portion_length = len(cidades_raw) // 4

    # Split the list into four parts
    cidades_part1 = cidades_raw[:portion_length]
    cidades_part2 = cidades_raw[portion_length:2*portion_length]
    cidades_part3 = cidades_raw[2*portion_length:3*portion_length]
    cidades_part4 = cidades_raw[3*portion_length:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_cidade_part1 = executor.submit(
            obter_dados_cidade, cidades_part1)
        future_cidade_part2 = executor.submit(
            obter_dados_cidade, cidades_part2)
        future_cidade_part3 = executor.submit(
            obter_dados_cidade, cidades_part3)
        future_cidade_part4 = executor.submit(
            obter_dados_cidade, cidades_part4)

        return_cidade_part1 = future_cidade_part1.result()
        return_cidade_part2 = future_cidade_part2.result()
        return_cidade_part3 = future_cidade_part3.result()
        return_cidade_part4 = future_cidade_part4.result()

        dados_clima = [*return_cidade_part1, *return_cidade_part2,
                       *return_cidade_part3, *return_cidade_part4]

        df = pd.DataFrame(dados_clima)
        df.to_csv('recomendacoes_materiais_construcao.csv', index=False)

        print("\n>>> Recomendações de materiais salvos com sucesso em 'recomendacoes_materiais_construcao.csv'.")


# Previsão

# total_temp = 0
# total_humidity = 0
# total_wind_speed = 0

# for cidade in cidades:
#     data = obter_data_clima(cidade)
#     if data:
#         for forecast in data['list']:
#             total_temp += forecast['main']['temp']
#             total_humidity += forecast['main']['humidity']
#             total_wind_speed += forecast['wind']['speed']

#             num_forecasts = len(data['list'])
#             # Calcular as médias
#             avg_temp = total_temp / num_forecasts
#             avg_humidity = total_humidity / num_forecasts
#             avg_wind_speed = total_wind_speed / num_forecasts

#     total_temp = 0
#     total_humidity = 0
#     total_wind_speed = 0
