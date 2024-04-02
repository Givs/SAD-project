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

    # Baixa temperatura, baixa velocidade do vento, baixa umidade:
    if temperatura < 10 and umidade < 30 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos, tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons quentes como marrom, terracota, bege"
        materiais_recomendados['Madeiras'] = "Cedro, pinho"
    # Baixa temperatura, alta velocidade do vento, baixa umidade:
    elif temperatura < 10 and umidade < 30 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos estruturais"
        materiais_recomendados['Telhas'] = "Telhas de metal, telhas de cerâmica com fixações adicionais"
        materiais_recomendados['Metais'] = "Alumínio, aço inoxidável"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, preto, branco"
        materiais_recomendados['Madeiras'] = "Ipê, cumaru"
    # Baixa temperatura, baixa velocidade do vento, alta umidade:
    elif temperatura < 10 and umidade >= 80 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos de concreto"
        materiais_recomendados['Telhas'] = "Telhas de ardósia"
        materiais_recomendados['Metais'] = "Alumínio com revestimento resistente à corrosão"
        materiais_recomendados['Cor'] = "Tons claros como branco, azul claro, verde claro"
        materiais_recomendados['Madeiras'] = "Teca, mogno"
    # Baixa temperatura, alta velocidade do vento, alta umidade:
    elif temperatura < 10 and umidade >= 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos com alta resistência à compressão"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica com fixações reforçadas"
        materiais_recomendados['Metais'] = "Aço inoxidável, titânio"
        materiais_recomendados['Cor'] = "Tons escuros como verde escuro, marinho, carvão"
        materiais_recomendados['Madeiras'] = "Sucupira, jatobá"
    # Alta temperatura, baixa velocidade do vento, baixa umidade:
    elif temperatura >= 30 and umidade < 30 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos refratários"
        materiais_recomendados['Telhas'] = "Telhas de terracota"
        materiais_recomendados['Metais'] = "Aço corten"
        materiais_recomendados['Cor'] = "Tons terrosos como ocre, terracota, marrom avermelhado"
        materiais_recomendados['Madeiras'] = "Mogno, cedro vermelho"
    # Alta temperatura, alta velocidade do vento, baixa umidade:
    elif temperatura >= 30 and umidade < 30 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários de alta densidade"
        materiais_recomendados['Telhas'] = "Telhas de metal com isolamento térmico"
        materiais_recomendados['Metais'] = "Ligas de níquel, ferro, titânio"
        materiais_recomendados['Cor'] = "Tons claros e reflexivos como branco, prateado, cinza claro"
        materiais_recomendados['Madeiras'] = "Louro, pau-rosa"
    # Alta temperatura, baixa velocidade do vento, alta umidade:
    elif temperatura >= 30 and umidade >= 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários especiais com alta resistência térmica e à umidade"
        materiais_recomendados['Telhas'] = "Telhas de metal com isolamento térmico e reforço adicional"
        materiais_recomendados['Metais'] = "Aço inoxidável de alta qualidade"
        materiais_recomendados['Cor'] = "Tons neutros e claros para minimizar a absorção de calor, como branco, cinza claro, verde claro.Tons neutros e claros para minimizar a absorção de calor, como branco, cinza claro, verde claro"
        materiais_recomendados['Madeiras'] = "Teca tratada, cedro"
    # Média temperatura, baixa velocidade do vento, baixa umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade < 30 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, bege"
        materiais_recomendados['Madeiras'] = "Pinho, cedro"
    # Baixa temperatura, média velocidade do vento, baixa umidade:
    elif temperatura < 10 and umidade < 30 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos, tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons quentes como marrom, terracota, bege"
        materiais_recomendados['Madeiras'] = "Cedro, pinho"
    # Baixa temperatura, baixa velocidade do vento, média umidade:
    elif temperatura < 10 and umidade >= 30 and umidade < 80 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, branco"
        materiais_recomendados['Madeiras'] = "Pinho, abeto"
    # Média temperatura, média velocidade do vento, baixa umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade < 30 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, bege"
        materiais_recomendados['Madeiras'] = "Pinho, cedro"
    # Média temperatura, baixa velocidade do vento, média umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 30 and umidade < 80 and velocidade_vento < 24:
        materiais_recomendados['Tijolos'] = "Tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, branco"
        materiais_recomendados['Madeiras'] = "Pinho, abeto"
    # Baixa temperatura, média velocidade do vento, média umidade:
    elif temperatura < 10 and umidade >= 30 and umidade < 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos de argila"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica"
        materiais_recomendados['Metais'] = "Aço galvanizado"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, branco"
        materiais_recomendados['Madeiras'] = "Pinho, abeto"
    # Média temperatura, média velocidade do vento, média umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 30 and umidade < 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos de argila, tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica, telhas de concreto"
        materiais_recomendados['Metais'] = "Aço galvanizado, alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, branco, bege"
        materiais_recomendados['Madeiras'] = "Pinho, abeto, cedro"
    # Média temperatura, alta velocidade do vento, alta umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos reforçados"
        materiais_recomendados['Telhas'] = "Telhas de cerâmica com fixações reforçadas"
        materiais_recomendados['Metais'] = "Aço inoxidável, alumínio"
        materiais_recomendados['Cor'] = "Tons escuros como verde escuro, marinho"
        materiais_recomendados['Madeiras'] = "Jatobá, ipê"
    # Alta temperatura, média velocidade do vento, alta umidade:
    elif temperatura >= 30 and umidade >= 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários"
        materiais_recomendados['Telhas'] = "Telhas de terracota"
        materiais_recomendados['Metais'] = "Aço corten"
        materiais_recomendados['Cor'] = "Tons terrosos como ocre, terracota, marrom avermelhado"
        materiais_recomendados['Madeiras'] = "Mogno, cedro vermelho"
    # Alta temperatura, alta velocidade do vento, média umidade:
    elif temperatura >= 30 and umidade >= 30 and umidade < 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários de alta densidade"
        materiais_recomendados['Telhas'] = "Telhas de metal com isolamento térmico"
        materiais_recomendados['Metais'] = "Ligas de níquel, ferro, titânio"
        materiais_recomendados['Cor'] = "Tons claros e reflexivos como branco, prateado, cinza claro"
        materiais_recomendados['Madeiras'] = "Louro, pau-rosa"
    # Média temperatura, média velocidade do vento, alta umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, bege"
        materiais_recomendados['Madeiras'] = "Pinho, cedro"
    # Média temperatura, alta velocidade do vento, média umidade:
    elif temperatura >= 10 and temperatura < 30 and umidade >= 30 and umidade < 80 and velocidade_vento >= 55:
        materiais_recomendados['Tijolos'] = "Tijolos cerâmicos"
        materiais_recomendados['Telhas'] = "Telhas cerâmicas, telhas de concreto"
        materiais_recomendados['Metais'] = "Alumínio"
        materiais_recomendados['Cor'] = "Tons neutros como cinza, bege"
        materiais_recomendados['Madeiras'] = "Pinho, cedro"
    # Alta temperatura, média velocidade do vento, média umidade:
    elif temperatura >= 30 and umidade >= 30 and umidade < 80 and velocidade_vento >= 24 and velocidade_vento < 55:
        materiais_recomendados['Tijolos'] = "Tijolos refratários"
        materiais_recomendados['Telhas'] = "Telhas de terracota"
        materiais_recomendados['Metais'] = "Aço corten"
        materiais_recomendados['Cor'] = "Tons terrosos como ocre, terracota, marrom avermelhado"
        materiais_recomendados['Madeiras'] = "Mogno, cedro vermelho"

    return materiais_recomendados
