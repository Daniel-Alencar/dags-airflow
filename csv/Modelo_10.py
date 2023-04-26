import pandas as pd

import warnings
warnings.filterwarnings("ignore")

import locale
locale.setlocale(locale.LC_ALL, '')

path = "csv/Bases/formatted_data"
extension = ".csv"
path_to_dataframe = path + extension

data = pd.read_csv(path_to_dataframe)

number_mes_inicial = 1

colunas = [
  "Valores reais",
  "Valores preditos",
  "Erros relativos",
  "Meses",
  "Marca",
  "Modelo",
  "Ano-modelo"
]

# Variáveis de controle
primeiros_meses = []
ultimos_meses = []
previsao = []
meses = []

# Percorrer Dataframe
for index, item in data.iterrows():
  value_mes_inicial = ""
  value_mes_final = ""

  while True:
    value_mes_inicial = item[f"Mes {number_mes_inicial}"]
    value_mes_final = item[f"Mes {number_mes_inicial + 12}"]

    if(pd.isna(value_mes_inicial) != True and pd.isna(value_mes_final) != True):
      meses.append(f"Mes {number_mes_inicial + 12}")
      number_mes_inicial = 1
      break
    
    if(number_mes_inicial + 12 >= 36):
      meses.append(f"Mes {1 + 12}")

      value_mes_inicial = item[f"Mes {1}"]
      value_mes_final = item[f"Mes {1 + 12}"]
      
      number_mes_inicial = 1
      break

    number_mes_inicial += 1

  try:
    value1 = locale.atof(value_mes_inicial)
  except:
    value1 = None

  try:
    value2 = locale.atof(value_mes_final)
  except:
    value2 = None
  
  primeiros_meses.append(value1)
  ultimos_meses.append(value2)


# Fazer cálculos
for i in range(len(primeiros_meses)):
  try:
    value = primeiros_meses[i] * 0.9
  except:
    value = None
  previsao.append(value)

# Adicionar ao banco de dados
new_data = pd.DataFrame(
  columns = colunas
)
dados = []

for index, item in data.iterrows():
  try:
    erro_relativo = (abs(previsao[index] - ultimos_meses[index])) / ultimos_meses[index]
  except:
    erro_relativo = None

  dados.append(
    {
      colunas[0]: ultimos_meses[index],
      colunas[1]: previsao[index],
      colunas[2]: erro_relativo,
      colunas[3]: meses[index],
      colunas[4]: data.iloc[index]["Marca"],
      colunas[5]: data.iloc[index]["Modelo"],
      colunas[6]: data.iloc[index]["Ano-modelo"],
    }
  )

new_data = new_data.append(dados)
new_data.to_csv('csv/Modelos/Modelo3.csv', index=False, na_rep='NaN')

# Média de degradação