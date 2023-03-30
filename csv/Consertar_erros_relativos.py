import pandas as pd

path = "csv/Modelos/Modelo2 comprimido"
extension = ".csv"
path_to_dataframe = path + extension

data = pd.read_csv(path_to_dataframe)
data = data.drop('Erros relativos', axis=1)

# Variáveis de controle
erros_relativos = []

for index, item in data.iterrows():
  erro = abs(item["Valores preditos"] - item["Valores reais"]) / item["Valores reais"]
  erros_relativos.append(erro)

# Adicionando ao Dataframe
data["Erros relativos"] = erros_relativos
data = data[[
  "Indice",
  "Valores reais",
  "Valores preditos",
  "Erros relativos",
  "Meses",
  "Marca",
  "Modelo",
  "Ano-modelo"
]]

path_to_dataframe = path + " " + "(teste)" + extension
data.to_csv(path_to_dataframe)