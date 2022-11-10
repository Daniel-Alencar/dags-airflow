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

class Web_Scrapping:
  # Constructor
  def __init__(self):
    # Site onde sera realizado o web scrapping
    self.url = "https://veiculos.fipe.org.br/"

    self.anos = [
      2020
    ]
    self.meses = [
      "janeiro"
    ]

    self.anos_modelo = [
      2020, 2021, "zero"
    ]

    option = Options()
    option.headless = False

    self.driver = webdriver.Firefox(options=option)
    self.wait = WebDriverWait(self.driver, 10)

  # Configura inicialmente o web_scrapping
  def setup(self):
    # Carregar a página
    self.driver.get(self.url)
    time.sleep(3)

    # Zoom In
    self.driver.set_context("chrome")
    win = self.driver.find_element(By.TAG_NAME, "html")
    for i in range(0, 7):
      win.send_keys(Keys.CONTROL + "-")
    self.driver.set_context("content")

    # Selecionar opcao de busca de carros
    self.driver.find_element(By.CSS_SELECTOR, selectors_html.cars_selector).click()
    time.sleep(1)

    # Seleciona o periodo
    self.driver.find_element(By.CSS_SELECTOR, selectors_html.time_period_selector).click()
    time.sleep(1)

  # Retorna um dicionário com os valores correspondentes
  def search_vehicle_information(self, marca, modelo):

    vehicle_information = {
      "marca": marca,
      "modelo": modelo,
      "anos": {}
    }

    for ano_busca in self.anos:
      vehicle_information['anos'][ano_busca] = {}

      for mes_busca in self.meses:
        vehicle_information['anos'][ano_busca][mes_busca] = {}

        # Seleciona o input do periodo
        self.driver.find_element(By.CSS_SELECTOR, selectors_html.input_time_period_selector).send_keys(f"{mes_busca}/{ano_busca}")
        time.sleep(3)

        # Seleciona o primeiro item do período
        elemento = self.wait.until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, selectors_html.item_time_period_selector))
        )
        elemento.click()

        # Seleciona o seletor das marcas
        self.driver.find_element(By.CSS_SELECTOR, selectors_html.brand_selector).click()
        time.sleep(1)
        
        # Filtro da marca desejada
        self.driver.find_element(By.CSS_SELECTOR, selectors_html.input_brand_selector).send_keys(marca)
        time.sleep(1)

        # Seleciona a primeira marca disponivel (marca desejada)
        self.driver.find_element(By.CSS_SELECTOR, selectors_html.item_brand_selector).click()
        time.sleep(1)

        # Seleciona o seletor dos modelos
        self.driver.find_element(By.CSS_SELECTOR, selectors_html.model_selector).click()
        time.sleep(1)

        # Filtro do modelo desejado
        self.driver.find_element(By.CSS_SELECTOR, selectors_html.input_model_selector).send_keys(modelo)
        time.sleep(1)      

        # Seleciona modelo desejado
        self.driver.find_element(By.CSS_SELECTOR, selectors_html.item_model_selector).click()
        time.sleep(1)

        for ano_modelo_busca in self.anos_modelo:

          print(f"Ano_modelo: {ano_modelo_busca}")

          if ano_modelo_busca == self.anos_modelo[0]:
            # Selecionar seletor dos anos-modelo
            self.driver.find_element(By.CSS_SELECTOR, selectors_html.year_model_selector).click()
            time.sleep(1)

          # Selecionar o input dos anos-modelo
          input = self.driver.find_element(By.CSS_SELECTOR, selectors_html.input_year_model_selector)
          time.sleep(1)

          for i in range(0, 4):
            input.send_keys(Keys.BACK_SPACE)

          input.send_keys(str(ano_modelo_busca))
          time.sleep(3)

          # Pega todos os filhos da <ul> de anos-modelo
          ul_year_model_element = self.driver.find_element(By.CSS_SELECTOR, selectors_html.ul_year_model_selector)
          ul_year_model_element_children = ul_year_model_element.find_elements(By.XPATH, "./*")

          time.sleep(3)
        
          if(ul_year_model_element_children[0].get_attribute("class") == 'no-results'):
            print(f"Quantidade de anos-modelo: 0")
          else:
            print(f"Quantidade de anos-modelo: {len(ul_year_model_element_children)}")

            # Selecionar o ano-modelo desejado
            self.driver.find_element(By.CSS_SELECTOR, selectors_html.item_year_model_selector).click()
            time.sleep(1)

            # Selecionar "Pesquisar"
            self.driver.find_element(By.CSS_SELECTOR, selectors_html.search_button_selector).click()
            time.sleep(1)

            # Pegar o preço do veiculo
            price = self.driver.find_element(By.CSS_SELECTOR, selectors_html.price_vehicle).text
            vehicle_information['anos'][ano_busca][mes_busca][ano_modelo_busca] = price

            print(f"Preço: {price}\n")

        # Limpar pesquisa
        try:
          element = self.driver.find_element(By.CSS_SELECTOR, selectors_html.clear_search_selector)
          element.click()
          print("Limpando a pesquisa!\n")
          time.sleep(1)
        except ElementNotInteractableException:
          print("Não foi possível limpar a pesquisa!\n")

    return vehicle_information




  # Leitura de Json com veiculos para buscar
  # Identificador básico: [marca][modelo_base][modelo_especifico]
  def get_vehicles_to_search(self):
    self.vehicles_to_search = util.read_json("json/vehicles_to_search.json")
    util.print_formatted_json(self.vehicles_to_search)

  # Leitura de Json com as informações dos veiculos
  def get_vehicles_with_price(self):
    self.vehicles_with_price = util.read_json("json/vehicles_with_price.json")
    util.print_formatted_json(self.vehicles_with_price)

  # Leitura de Json com indices de busca
  # marca, modelo_base e modelo_especifico
  def get_indices_de_busca(self):
    self.indices_de_busca = util.read_json("json/indices_de_busca.json")
    util.print_formatted_json(self.indices_de_busca)






  def check_indexes(self):
    try:
      print(
        self.vehicles_to_search
          [self.indices_de_busca["marca"]]["modelos_base"]
          [self.indices_de_busca["modelo_base"]]
          [self.indices_de_busca["modelo_especifico"]]
      )
    except:
      return False
    return True






  def update_vehicles_with_price_json(self):
    with open("json/vehicles_with_price.json", "w") as jsonFile:
      json.dump(self.vehicles_with_price, jsonFile, indent=2)
  
  def update_indices_de_busca_json(self):
    with open("json/indices_de_busca.json", "w") as jsonFile:
      json.dump(self.indices_de_busca, jsonFile, indent=2)






  def update_indexes(self):
    self.indices_de_busca["modelo_especifico"] += 1
    indexes_OK = self.check_indexes()

    if indexes_OK == False:
      self.indices_de_busca["modelo_base"] += 1
      self.indices_de_busca["modelo_especifico"] = 0
      indexes_OK = self.check_indexes()

      if indexes_OK == False:
        self.indices_de_busca["marca"] += 1
        self.indices_de_busca["modelo_base"] = 0
        self.indices_de_busca["modelo_especifico"] = 0
        indexes_OK = self.check_indexes()

        if indexes_OK == False:
          self.indices_de_busca["marca"] = None
          self.indices_de_busca["modelo_base"] = None
          self.indices_de_busca["modelo_especifico"] = None

    print(self.indices_de_busca)
    self.update_indices_de_busca_json()

    return indexes_OK


  # Faz a execução do Web Scrapping de acordo com o que desejamos
  def execution(self):
    self.setup()

    print(self.indices_de_busca)
    while self.check_indexes():
      vehicle_information = self.search_vehicle_information(
        
        # marca
        self.vehicles_to_search
          [self.indices_de_busca["marca"]]["marca"],
        
        # modelo
        self.vehicles_to_search
          [self.indices_de_busca["marca"]]["modelos_base"]
          [self.indices_de_busca["modelo_base"]]
          [self.indices_de_busca["modelo_especifico"]]
      )
      util.print_formatted_json(vehicle_information)

      self.vehicles_with_price.append(vehicle_information)
      self.update_vehicles_with_price_json()

      if self.update_indexes() == False:
        break

    # Fechamento de execução do web_scrapping
    self.driver.quit()
