# Sistema de Apoio à Decisão para Materiais de Construção

Este projeto é um protótipo de Sistema de Apoio à Decisão (SAD) que recomenda materiais de construção baseados nas condições climáticas de uma cidade específica. Utiliza dados climáticos em tempo real fornecidos pela API do OpenWeatherMap para analisar as condições locais, incluindo temperatura, umidade e velocidade do vento, e sugere materiais adequados para a construção baseado nessas condições.

## Requisitos

Para executar este script, você precisará de Python 3 e da biblioteca `requests`. Certifique-se de que o Python 3 esteja instalado em seu sistema. Você pode verificar isso executando:

```bash
python3 --version
```
Se você não tem o Python instalado, visite python.org para baixar e instalar a versão mais recente.

## Instalação

### Biblioteca requests

Este projeto depende da biblioteca requests para fazer chamadas à API.


### Obter uma Chave de API do OpenWeatherMap

Para acessar as informações climáticas, você precisará de uma chave de API do OpenWeatherMap. Siga estes passos para obter uma:

    - Visite https://openweathermap.org/ e crie uma conta.
    - Navegue até a seção API Keys de seu painel.
    - Crie uma nova chave de API ou use uma existente.
    - Substitua o valor de api_key no arquivo main.py pela sua chave de API real.

### Executando o Script

Depois de configurar sua chave de API e instalar as dependências necessárias, você pode executar o script usando o seguinte comando:

```bash
python3 main.py
```