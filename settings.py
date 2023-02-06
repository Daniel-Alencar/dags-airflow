import datetime as dt

### PODEM MUDAR
absolute_path = "/home/engenheiro/airflow/dags/"

verbose = True
headless = False

# Começa em 0
computer_id = 2
mini_batch = 1
retries = 30
retry_delay = dt.timedelta(seconds = 20)

### NÃO PODEM MUDAR
vehicles_to_search_path = f"{absolute_path}json/vehicles_to_search.json"
vehicles_with_price_path = f"{absolute_path}json/vehicles_with_price.json"
modelo_atual_path = f"{absolute_path}json/modelo_atual.json"
incomplete_path = f"{absolute_path}json/incomplete.json"
incomplete_to_search_path = f"{absolute_path}json/incomplete_to_search.json"
data_path = f"{absolute_path}csv/data.csv"
data_without_null_path = f"{absolute_path}csv/data_without_null.csv"

number_of_computers = 5
number_of_years = 3

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
