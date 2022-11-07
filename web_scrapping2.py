from airflow import DAG
import datetime as dt
from airflow.operators.python import PythonOperator

import time
import json
import util
import selectors_html

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Site onde sera realizado o web scrapping
url = "https://veiculos.fipe.org.br/"


anos = [
  2020
]

meses = [
  "janeiro"
]

anos_modelo = [
  2020, 2021, "zero"
]




option = Options()
option.headless = False

driver = webdriver.Firefox(options=option)
wait = WebDriverWait(driver, 10)


# Configura inicialmente o web_scrapping
def setup():
  # Carregar a página
  driver.get(url)
  time.sleep(3)

  # Zoom In
  driver.set_context("chrome")
  win = driver.find_element(By.TAG_NAME, "html")
  for i in range(0, 7):
    win.send_keys(Keys.CONTROL + "-")
  driver.set_context("content")

  # Selecionar opcao de busca de carros
  driver.find_element(By.CSS_SELECTOR, selectors_html.cars_selector).click()
  time.sleep(1)

  # Seleciona o periodo
  driver.find_element(By.CSS_SELECTOR, selectors_html.time_period_selector).click()
  time.sleep(1)

# Retorna um dicionário com os valores correspondentes
def get_model_prices(anos, meses, marca, modelo, anos_modelo):

  vehicle_information = {
    "marca": marca,
    "modelo": modelo,
    "anos": {}
  }

  for ano_busca in anos:
    vehicle_information['anos'][ano_busca] = {}

    for mes_busca in meses:
      vehicle_information['anos'][ano_busca][mes_busca] = {}

      # Seleciona o input do periodo
      driver.find_element(By.CSS_SELECTOR, selectors_html.input_time_period_selector).send_keys(f"{mes_busca}/{ano_busca}")
      time.sleep(3)

      # Seleciona o primeiro item do período
      elemento = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selectors_html.item_time_period_selector))
      )
      elemento.click()

      # Seleciona o seletor das marcas
      driver.find_element(By.CSS_SELECTOR, selectors_html.brand_selector).click()
      time.sleep(1)
      
      # Filtro da marca desejada
      driver.find_element(By.CSS_SELECTOR, selectors_html.input_brand_selector).send_keys(marca)
      time.sleep(1)

      # Seleciona a primeira marca disponivel (marca desejada)
      driver.find_element(By.CSS_SELECTOR, selectors_html.item_brand_selector).click()
      time.sleep(1)

      # Seleciona o seletor dos modelos
      driver.find_element(By.CSS_SELECTOR, selectors_html.model_selector).click()
      time.sleep(1)

      # Filtro do modelo desejado
      driver.find_element(By.CSS_SELECTOR, selectors_html.input_model_selector).send_keys(modelo)
      time.sleep(1)      

      # Seleciona modelo desejado
      driver.find_element(By.CSS_SELECTOR, selectors_html.item_model_selector).click()
      time.sleep(1)

      for ano_modelo_busca in anos_modelo:

        print(f"Ano_modelo: {ano_modelo_busca}")

        if ano_modelo_busca == anos_modelo[0]:
          # Selecionar seletor dos anos-modelo
          driver.find_element(By.CSS_SELECTOR, selectors_html.year_model_selector).click()
          time.sleep(1)

        # Selecionar o input dos anos-modelo
        input = driver.find_element(By.CSS_SELECTOR, selectors_html.input_year_model_selector)
        time.sleep(1)

        for i in range(0, 4):
          input.send_keys(Keys.BACK_SPACE)

        input.send_keys(str(ano_modelo_busca))
        time.sleep(3)

        # Pega todos os filhos da <ul> de anos-modelo
        ul_year_model_element = driver.find_element(By.CSS_SELECTOR, selectors_html.ul_year_model_selector)
        ul_year_model_element_children = ul_year_model_element.find_elements(By.XPATH, "./*")

        time.sleep(3)
      
        if(ul_year_model_element_children[0].get_attribute("class") == 'no-results'):
          print(f"Quantidade de anos-modelo: 0")
        else:
          print(f"Quantidade de anos-modelo: {len(ul_year_model_element_children)}")

          # Selecionar o ano-modelo desejado
          driver.find_element(By.CSS_SELECTOR, selectors_html.item_year_model_selector).click()
          time.sleep(1)

          # Selecionar "Pesquisar"
          driver.find_element(By.CSS_SELECTOR, selectors_html.search_button_selector).click()
          time.sleep(1)

          # Pegar o preço do veiculo
          price = driver.find_element(By.CSS_SELECTOR, selectors_html.price_vehicle).text
          vehicle_information['anos'][ano_busca][mes_busca][ano_modelo_busca] = price

          print(f"Preço: {price}\n")

      # Limpar pesquisa
      try:
        element = driver.find_element(By.CSS_SELECTOR, selectors_html.clear_search_selector)
        element.click()
        print("Limpando a pesquisa!\n")
        time.sleep(1)
      except ElementNotInteractableException:
        print("Não foi possível limpar a pesquisa!\n")

  return vehicle_information

# Faz a execução do Web Scrapping de acordo com o que desejamos
def execution():
  # Identificador básico: [marca][modelo_base][modelo_especifico]
  vehicles_to_search = util.read_json("json/vehicles_to_search.json")
  vehicles_with_price = util.read_json("json/vehicles_with_price.json")
  # Busca dos indices de: marca, modelo_base e modelo_especifico
  indices_de_busca = util.read_json("json/indices_de_busca.json")
  print(indices_de_busca)

  setup()
  while util.check_indexes(vehicles_to_search, indices_de_busca):
    vehicle_information = get_model_prices(
      anos, 
      meses, 
      vehicles_to_search
        [indices_de_busca["marca"]]["marca"],
      vehicles_to_search
        [indices_de_busca["marca"]]["modelos_base"]
        [indices_de_busca["modelo_base"]]
        [indices_de_busca["modelo_especifico"]],
      anos_modelo
    )

    vehicle_information_formatted = json.dumps(vehicle_information, indent=2)
    print(vehicle_information_formatted)

    vehicles_with_price.append(vehicle_information)
    with open("json/vehicles_with_price.json", "w") as jsonFile:
      json.dump(vehicles_with_price, jsonFile, indent=2)
    print("\n=======================\n")

    if util.update_indexes(vehicles_to_search, indices_de_busca) == False:
      break
    indices_de_busca = util.read_json("json/indices_de_busca.json")

  # Fechamento de execução do web_scrapping
  driver.quit()


dag = DAG(
  dag_id = "web_scrapping2",
  start_date = dt.datetime(year=2022, month=11, day=5),
  end_date = dt.datetime(year=2022, month=11, day=10),
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'task_1',
  python_callable = execution,
  dag = dag
)

task_1