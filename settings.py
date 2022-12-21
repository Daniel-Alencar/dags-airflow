absolute_path = "/home/engenheiro/airflow/dags/"

vehicles_to_search_path = f"{absolute_path}json/vehicles_to_search.json"
vehicles_with_price_path = f"{absolute_path}json/vehicles_with_price.json"
modelo_atual_path = f"{absolute_path}json/modelo_atual.json"

verbose = True
headless = True

# NÃO PODEM MUDAR
number_of_computers = 5
number_of_years = 3

# PODEM MUDAR

# Começa em 0
computer_id = 1
mini_batch = 8

meses = [
  "janeiro", "fevereiro", "março", "abril", "maio", "junho",
  "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

anos_modelo = [
  2015, 2016, 2017, 2018, 2019, 2020
]

structure_columns = ['Marca', 'Modelo', 'Ano-modelo']
for index in range(number_of_years * len(meses)):
  structure_columns.append(f'Mes {index + 1}')