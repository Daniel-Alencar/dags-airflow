import pandas as pd
import numpy as np

from sklearn.metrics import mean_absolute_percentage_error

path = "csv/Modelos/Modelo1 comprimido"
extension = ".csv"
path_to_dataframe = path + extension

data = pd.read_csv(path_to_dataframe)
marca = "Jeep"

# Variáveis de controle
valores_preditos = []
valores_reais = []

# Definição da análise estatística R square
def r2Score(actual, predict):
  correlationMatrix = np.corrcoef(actual, predict)
  corrNormalized = correlationMatrix[0, 1]
  rSquare = corrNormalized ** 2
  
  return rSquare

# Percorrer Dataframe
for index, item in data.iterrows():
  if (marca == item["Marca"]):
    valores_reais.append(float(item["Valores reais"]))
    valores_preditos.append(float(item["Valores preditos"]))

# Fazer cálculos
print(f"R2: {r2Score(valores_reais, valores_preditos)}")
print(f"MAPE: {mean_absolute_percentage_error(valores_reais, valores_preditos)}")