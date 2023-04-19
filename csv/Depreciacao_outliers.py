import pandas as pd

import locale
locale.setlocale(locale.LC_ALL, '')

path = "csv/Modelos/Modelo1 comprimido (limitado)"
extension = ".csv"
path_to_dataframe = path + extension

marcas = [
  "Audi",
  "BMW",
  "CAOA Chery"
]

new_data = pd.DataFrame(columns=[
  "Marca",
  "Modelo",
  "Ano-modelo",
  "Amplitude"
])


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
      marcas[i],
      data.iloc[index]["Modelo"],
      data.iloc[index]["Ano-modelo"],
      porcentagem
    ]
    new_data.loc[len(new_data)] = vetor
    index += 1

print(new_data)
