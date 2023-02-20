import pandas as pd
import util
from settings import anos_modelo

meses_indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
vehicles = util.read_json("json/vehicles_only_from_2016.json")

marca = vehicles[0]["marca"]
modelo = vehicles[0]["modelos_base"][0][3]

ano_modelo = anos_modelo[0]
ano_referencia = anos_modelo[0] + 0
mes_referencia = meses_indices[0]

# Buscando os dados
values = pd.read_csv("csv/tabela-fipe.csv")
values = values.loc[values['modelo'] == modelo]
values = values.loc[values['anoModelo'] == ano_modelo]
values = values.loc[values['mesReferencia'] == mes_referencia]
values = values.loc[values['anoReferencia'] == ano_referencia]

search = {
  'marca': marca,
  'modelo': modelo,
  'ano_modelo': ano_modelo,
  'ano_referencia': ano_referencia,
  'mes_referencia': mes_referencia
}
util.print_formatted_json(search)
print("\n")
print(values)

try:
  # Ajustando a string preço
  value = str(values.iloc[0]['valor'])
  value = value.replace(".", ",")

  value0 = value[-2:]

  intermediate_value = value[:-2]
  value1 = intermediate_value[-3:]
  value2 = intermediate_value[:-3]

  value = value2 + '.' + value1 + value0
  value = f"R$ {value}0"
  
  search['Preço'] = value
  print("")
  util.print_formatted_json(search)

except:
  print("\nNão existe esse valor na tabela!")
