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

    porcentagem = ((value1 - value2) / value1) * 100
    porcentagem = round(porcentagem, 2)

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

  marca_dataset = data.iloc[index]["Marca"]

  marca_diferente = True
  for marca in marcas:
    if(marca_dataset == marca):
      marca_diferente = False

  if(marca_diferente):
    modelo = data.iloc[index]["Modelo"]
    ano_modelo = data.iloc[index]["Ano-modelo"]
    value1 = data.iloc[index]["Valores preditos"]

    if(data.iloc[index + 11]["Modelo"] == modelo and data.iloc[index + 11]["Ano-modelo"] == ano_modelo):

      index += 11
      value2 = data.iloc[index]["Valores preditos"]

      porcentagem = ((value1 - value2) / value1) * 100
      porcentagem = round(porcentagem, 2)

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

# Calculando as médias de depreciação
data_outliers = pd.read_csv('csv/depreciacao_outliers.csv')
data_marcas = pd.read_csv('csv/depreciacao_marcas.csv')

amplitude_outliers = data_outliers['Amplitude'].tolist()
amplitude_marcas = data_marcas['Amplitude'].tolist()

media_outliers = sum(amplitude_outliers) / len(amplitude_outliers)
media_marcas = sum(amplitude_marcas) / len(amplitude_marcas)

print("")
print(f"Média das taxas de depreciação dos outliers: {media_outliers}")
print(f"Média das taxas de depreciação das outras marcas: {media_marcas}")