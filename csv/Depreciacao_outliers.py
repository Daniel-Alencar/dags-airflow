import pandas as pd

import locale
locale.setlocale(locale.LC_ALL, '')

path = "csv/Modelos/Modelo1 comprimido (limitado)"
extension = ".csv"
path_to_dataframe = path + extension

new_data = pd.DataFrame(columns=[
  "Marca",
  "Modelo",
  "Ano-modelo",
  "Amplitude"
])
new_data_for_brands = pd.DataFrame(columns=[
  "Marca",
  "Modelo",
  "Ano-modelo",
  "Amplitude"
])


marcas = [
  "Audi",
  "BMW",
  "CAOA Chery"
]

# Calculando depreciação nos outliers
for i in range(len(marcas)):
  data = pd.read_csv(path_to_dataframe)
  data = data.loc[data['Marca'] == marcas[i]]
  index = 0

  while True:
    if(index == len(data)):
      break

    value1 = data.iloc[index]["Valores preditos"]
    index += 11
    value2 = data.iloc[index]["Valores preditos"]

    porcentagem = (value1 - value2) / value1

    vetor = [
      data.iloc[index]["Marca"],
      data.iloc[index]["Modelo"],
      data.iloc[index]["Ano-modelo"],
      porcentagem
    ]
    new_data.loc[len(new_data)] = vetor
    index += 1

print(new_data)
new_data.to_csv("csv/depreciacao_outliers.csv", index=False)



# Calculando depreciação nos outros veículos
data = pd.read_csv(path_to_dataframe)

index = 0
while True:
  if(index >= len(data.index)):
    break

  marca = data.iloc[index]["Marca"]

  marca_diferente = True
  for item in marcas:
    if(marca == item):
      marca_diferente = False

  if(marca_diferente):
    value1 = data.iloc[index]["Valores preditos"]
    index += 11
    value2 = data.iloc[index]["Valores preditos"]

    porcentagem = (value1 - value2) / value1

    vetor = [
      data.iloc[index]["Marca"],
      data.iloc[index]["Modelo"],
      data.iloc[index]["Ano-modelo"],
      porcentagem
    ]
    new_data_for_brands.loc[len(new_data_for_brands)] = vetor
  
  index += 1

print(new_data_for_brands)
new_data_for_brands.to_csv("csv/depreciacao_marcas.csv", index=False)