import pandas as pd
import numpy as np

import locale
locale.setlocale(locale.LC_ALL, '')

path = "csv/Bases/formatted_data"
extension = ".csv"
path_to_dataframe = path + extension

data = pd.read_csv(path_to_dataframe)
mes_inicial = "Mes 12"
mes_final = "Mes 24"

# Variáveis de controle
meses12 = []
meses24 = []
porcentagem = []

# Percorrer Dataframe
for index, item in data.iterrows():

  value_mes_inicial = item[mes_inicial].replace(",", "")
  value_mes_final = item[mes_inicial].replace(",", "")

  meses12.append(locale.atof(value_mes_inicial))
  meses24.append(locale.atof(value_mes_final))

# Fazer cálculos
for i in range(len(meses12)):
  value = (meses24[i] / meses12[i]) * 100
  porcentagem.append(value)

print(meses12)