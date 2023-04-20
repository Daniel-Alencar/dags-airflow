import pandas as pd

import warnings
warnings.filterwarnings("ignore")

import locale
locale.setlocale(locale.LC_ALL, '')

path = "csv/Bases/formatted_data"
extension = ".csv"
path_to_dataframe = path + extension

data = pd.read_csv(path_to_dataframe)
mes_inicial = "Mes 1"
mes_final = "Mes 36"

# Variáveis de controle
primeiro_mes = []
ultimo_mes = []
depreciacao = []

# Percorrer Dataframe
for index, item in data.iterrows():

  value_mes_inicial = item[mes_inicial]
  value_mes_final = item[mes_final]

  try:
    value1 = locale.atof(value_mes_inicial)
    value2 = locale.atof(value_mes_final)
  except:
    value1 = None
    value2 = None
  
  primeiro_mes.append(value1)
  ultimo_mes.append(value2)


# Fazer cálculos
for i in range(len(primeiro_mes)):
  try:
    value = ((primeiro_mes[i] - ultimo_mes[i]) / primeiro_mes[i]) * 100
    value = round(value, 2)
  except:
    value = None
  depreciacao.append(value)

# Adicionar ao banco de dados
data = pd.read_csv(path_to_dataframe)
data["Depreciação"] = depreciacao
data.to_csv('csv/data_com_depreciação.csv', index=False, na_rep='NaN')

# Média de degradação
counter = 0
sum_depreciacao = 0
for item in depreciacao:
  if(item != None):
    sum_depreciacao += item
    counter += 1
media_depreciacao = sum_depreciacao / counter
media_depreciacao = round(media_depreciacao, 2)

print(f"Média das taxas de depreciação da base completa: {media_depreciacao}%")