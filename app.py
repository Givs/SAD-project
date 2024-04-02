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

    materiais_recomendados['Metais'] = "Aço galvanizado"
    materiais_recomendados['Madeiras'] = "Cedro, pinho"
    materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"

    
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

    #Baixa temperatura, baixa velocidade do vento, baixa umidade:
    if temperatura < 10 and umidade < 30 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos, tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons quentes como marrom, terracota, bege"
        materiais_recomendados['Madeiras'] = "Cedro, pinho"
    #Baixa temperatura, alta velocidade do vento, baixa umidade:
    elif temperatura < 10 and umidade < 30 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos estruturais"
        materiais_recomendados['Telhas'] = "Telhas de metal, telhas de cerâmica com fixações adicionais"
        materiais_recomendados['Metais'] = "Alumínio, aço inoxidável"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, preto, branco"
        materiais_recomendados['Madeiras'] = "Ipê, cumaru"
    #Baixa temperatura, baixa velocidade do vento, alta umidade:
    elif temperatura < 10 and umidade >= 80 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos de concreto"
        materiais_recomendados['Telhas'] = "Telhas de ardósia"
        materiais_recomendados['Metais'] = "Alumínio com revestimento resistente à corrosão"
        materiais_recomendados['Cor'] = "Tons claros como branco, azul claro, verde claro"
        materiais_recomendados['Madeiras'] = "Teca, mogno"
    #Baixa temperatura, alta velocidade do vento, alta umidade:
    elif temperatura < 10 and umidade >= 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos com alta resistência à compressão"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica com fixações reforçadas"
        materiais_recomendados['Metais'] = "Aço inoxidável, titânio"
        materiais_recomendados['Cor'] = "Tons escuros como verde escuro, marinho, carvão"
        materiais_recomendados['Madeiras'] = "Sucupira, jatobá"
    #Alta temperatura, baixa velocidade do vento, baixa umidade:
    elif temperatura >= 30 and umidade < 30 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos refratários"
        materiais_recomendados['Telhas'] = "Telhas de terracota"
        materiais_recomendados['Metais'] = "Aço corten"
        materiais_recomendados['Cor'] = "Tons terrosos como ocre, terracota, marrom avermelhado"
        materiais_recomendados['Madeiras'] = "Mogno, cedro vermelho"
    #Alta temperatura, alta velocidade do vento, baixa umidade:
    elif temperatura >= 30 and umidade < 30 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários de alta densidade"
        materiais_recomendados['Telhas'] = "Telhas de metal com isolamento térmico"
        materiais_recomendados['Metais'] = "Ligas de níquel, ferro, titânio"
        materiais_recomendados['Cor'] = "Tons claros e reflexivos como branco, prateado, cinza claro"
        materiais_recomendados['Madeiras'] = "Louro, pau-rosa"
    #Alta temperatura, baixa velocidade do vento, alta umidade:
    elif temperatura >= 30 and umidade >= 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários especiais com alta resistência térmica e à umidade"
        materiais_recomendados['Telhas'] = "Telhas de metal com isolamento térmico e reforço adicional"
        materiais_recomendados['Metais'] = "Aço inoxidável de alta qualidade"
        materiais_recomendados['Cor'] = "Tons neutros e claros para minimizar a absorção de calor, como branco, cinza claro, verde claro.Tons neutros e claros para minimizar a absorção de calor, como branco, cinza claro, verde claro"
        materiais_recomendados['Madeiras'] = "Teca tratada, cedro"
    #Média temperatura, baixa velocidade do vento, baixa umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade < 30 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, bege"
        materiais_recomendados['Madeiras'] = "Pinho, cedro"
    #Baixa temperatura, média velocidade do vento, baixa umidade:
    elif temperatura < 10 and umidade < 30 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos, tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons quentes como marrom, terracota, bege"
        materiais_recomendados['Madeiras'] = "Cedro, pinho"
    #Baixa temperatura, baixa velocidade do vento, média umidade:
    elif temperatura < 10 and umidade >= 30 and umidade < 80 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, branco"
        materiais_recomendados['Madeiras'] = "Pinho, abeto"
    #Média temperatura, média velocidade do vento, baixa umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade < 30 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, bege"
        materiais_recomendados['Madeiras'] = "Pinho, cedro"
    #Média temperatura, baixa velocidade do vento, média umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 30 and umidade < 80 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, branco"
        materiais_recomendados['Madeiras'] = "Pinho, abeto"
    #Baixa temperatura, média velocidade do vento, média umidade:
    elif temperatura < 10 and umidade >= 30 and umidade < 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, branco"
        materiais_recomendados['Madeiras'] = "Pinho, abeto"
    #Média temperatura, média velocidade do vento, média umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 30 and umidade < 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos de argila, tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica, telhas de concreto"
        materiais_recomendados['Metais'] = "Aço galvanizado, alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, branco, bege"
        materiais_recomendados['Madeiras'] = "Pinho, abeto, cedro"
    #Média temperatura, alta velocidade do vento, alta umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos reforçados"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica com fixações reforçadas"
        materiais_recomendados['Metais'] = "Aço inoxidável, alumínio"
        materiais_recomendados['Cor'] = "Tons escuros como verde escuro, marinho"
        materiais_recomendados['Madeiras'] = "Jatobá, ipê"
    #Alta temperatura, média velocidade do vento, alta umidade:
    elif temperatura >= 30 and umidade >= 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários"
        materiais_recomendados['Telhas'] = "Telhas de terracota"
        materiais_recomendados['Metais'] = "Aço corten"
        materiais_recomendados['Cor'] = "Tons terrosos como ocre, terracota, marrom avermelhado"
        materiais_recomendados['Madeiras'] = "Mogno, cedro vermelho"
    #Alta temperatura, alta velocidade do vento, média umidade:
    elif temperatura >= 30 and umidade >= 30 and umidade < 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários de alta densidade"
        materiais_recomendados['Telhas'] = "Telhas de metal com isolamento térmico"
        materiais_recomendados['Metais'] = "Ligas de níquel, ferro, titânio"
        materiais_recomendados['Cor'] = "Tons claros e reflexivos como branco, prateado, cinza claro"
        materiais_recomendados['Madeiras'] = "Louro, pau-rosa"
    #Média temperatura, média velocidade do vento, alta umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, bege"
        materiais_recomendados['Madeiras'] = "Pinho, cedro"
    #Média temperatura, alta velocidade do vento, média umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 30 and umidade < 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, bege"
        materiais_recomendados['Madeiras'] = "Pinho, cedro"
    #Alta temperatura, média velocidade do vento, média umidade:
    elif temperatura >= 30 and umidade >= 30 and umidade < 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários"
        materiais_recomendados['Telhas'] = "Telhas de terracota"
        materiais_recomendados['Metais'] = "Aço corten"
        materiais_recomendados['Cor'] = "Tons terrosos como ocre, terracota, marrom avermelhado"
        materiais_recomendados['Madeiras'] = "Mogno, cedro vermelho"

    
    return materiais_recomendados

cidades = ['Aracaju, BR', 'Nossa Senhora do Socorro, BR', 'Lagarto, BR', 'Itabaiana, BR', 'São Cristóvão, BR', 'Estância, BR', 'Nossa Senhora da Glória, BR', 
           'Propriá, BR', 'Itabaianinha, BR', 'Capela, BR', 'Simão Dias, BR', 'Nossa Senhora das Dores, BR', 'Poço Verde, BR', 'Tobias Barreto, BR', 'Umbaúba, BR', 
           'Campo do Brito, BR', 'Boquim, BR', 'Indiaroba, BR', 'Japaratuba, BR', 'Pedrinhas, BR', 'Maruim, BR', 'Siriri, BR', 'Pacatuba, BR', 
           'Rosário do Catete, BR', 'Monte Alegre de Sergipe, BR', 'Brejo Grande, BR', 'Salgado, BR', 'São Miguel do Aleixo, BR', 'Neópolis, BR', 'Areia Branca, BR', 
           'Moita Bonita, BR', 'Itabi, BR', 'Malhador, BR', 'Gararu, BR', 'Arauá, BR', 'Macambira, BR', 'Pedra Mole, BR', 'Cristinápolis, BR', 'Malhada dos Bois, BR', 
           'Nossa Senhora Aparecida, BR', 'Telha, BR', 'Cumbe, BR', 'Feira Nova, BR', 'Pinhão, BR', 'Lagoa Funda, BR', 'Poço Redondo, BR', 'Divina Pastora, BR', 
           'Ilha das Flores, BR', 'Canhoba, BR', 'Santa Rosa de Lima, BR', 'Nossa Senhora de Lourdes, BR', 'Pirambu, BR', 'São Francisco, BR', 'Carira, BR', 
           'Laranjeiras, BR', 'Riachão do Dantas, BR', 'Santa Luzia do Itanhy, BR', 'Porto da Folha, BR', 'Tomar do Geru, BR', 'Aquidabã, BR', 
           'Santana do São Francisco, BR', 'Carmópolis, BR', 'Macambira, BR', 'Canindé de São Francisco, BR', 'Siriri, BR', 'Pedra Branca, BR']

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

# Previsão
        
total_temp = 0
total_humidity = 0
total_wind_speed = 0

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

    total_temp = 0
    total_humidity = 0
    total_wind_speed = 0


df = pd.DataFrame(dados_clima)

df.to_csv('recomendacoes_materiais_construcao.csv', index=False)

print("Recomendações de materiais salvos com sucesso em 'recomendacoes_materiais_construcao.csv'.")
