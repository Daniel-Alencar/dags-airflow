import pandas as pd

path = "csv/Modelos/Modelo2 comprimido"
extension = ".csv"
path_to_dataframe = path + extension

data = pd.read_csv(path_to_dataframe)
marca = ""
modelo = ""
ano_modelo = 0

equal_values_counter = 0
# Quantidade de linhas que não serão apagadas de uma mesma marca, modelo e ano-modelo
number_of_rows_to_keep = 12

rows_indexes_to_delete = []

# Salvar os índices das linhas que quero excluir
for index, item in data.iterrows():
  if(marca != item["Marca"] or modelo != item["Modelo"] or ano_modelo != item["Ano-modelo"]):
    marca = item["Marca"]
    modelo = item["Modelo"]
    ano_modelo = item["Ano-modelo"]

    equal_values_counter = 1
  else:
    equal_values_counter += 1

    if equal_values_counter > number_of_rows_to_keep:
      rows_indexes_to_delete.append(index)

# Excluir as linhas desejadas
for index in rows_indexes_to_delete:
  data.drop(index, axis='index', inplace=True)
data = data.drop("Indice", axis=1)

# Fazer CSV a partir do novo Dataframe
path_to_dataframe = path + " " + "(limitado)" + extension
data.to_csv(path_to_dataframe)