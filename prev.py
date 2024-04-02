from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Supondo que você tenha os dados de temperatura, umidade e velocidade do vento em arrays separados
temperatura = [...]  # lista/array com as temperaturas
umidade = [...]      # lista/array com as umidades
velocidade_vento = [...]  # lista/array com as velocidades do vento

# Concatenar os dados em uma matriz de características X
X = np.column_stack((temperatura, umidade, velocidade_vento))

# Supondo que você tenha os dados de previsão para os próximos 30 dias
# Você precisaria preparar esses dados da mesma maneira que os dados históricos

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escolher e treinar o modelo (usando regressão linear como exemplo)
model = LinearRegression()
model.fit(X_train, y_train)

# Avaliar o modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Erro Quadrático Médio:", mse)

# Fazer previsões para os próximos 30 dias
# Suponha que você tenha os dados futuros em um array chamado X_future
# X_future deve ter o mesmo formato que X_train e X_test
previsoes_futuras = model.predict(X_future)
print("Previsões para os próximos 30 dias:", previsoes_futuras)
