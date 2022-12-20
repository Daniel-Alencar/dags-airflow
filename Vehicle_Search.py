import time
import util
import selectors_html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import verbose, headless

class Vehicle_Search():
  # Constructor
  def __init__(self):

    # Site onde sera realizado o web scrapping
    self.url = "https://veiculos.fipe.org.br/"

    option = Options()
    option.headless = headless
    self.driver = webdriver.Firefox(options=option)
    self.wait = WebDriverWait(self.driver, 10)

    self.words = ["Aut.", "Mec."]

  # Configurar inicialmente o web_scrapping
  def setup(self):
    # Carregar a página
    self.driver.get(self.url)
    time.sleep(3)

    # Selecionar opcao de busca de carros
    self.driver.find_element(By.CSS_SELECTOR, selectors_html.cars_selector).click()
    time.sleep(1)

    # Seleciona o periodo
    self.driver.find_element(By.CSS_SELECTOR, selectors_html.time_period_selector).click()
    time.sleep(1)

  # Listar todos os modelos que possuem aquele modelo_base [(0, nome_0)]
  def get_models_from_model_base(self, marca, modelo_base, mes_busca, ano_busca):

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
    
    # Pega todos os filhos da <ul> de anos-modelo
    ul_brand_model_element = self.driver.find_element(By.CSS_SELECTOR, selectors_html.ul_brand_model_element_selector)
    ul_brand_model_element_children = ul_brand_model_element.find_elements(By.XPATH, "./*")

    models_names = []

    if(ul_brand_model_element_children[0].get_attribute("class") == 'no-results'):
      if verbose:
        print(f"Quantidade de marcas: 0")
    else:
      if verbose:
        print(f"Quantidade de marcas: {len(ul_brand_model_element_children)}")

      # Seleciona a primeira marca disponivel (marca desejada)
      self.driver.find_element(By.CSS_SELECTOR, selectors_html.item_brand_selector).click()
      time.sleep(1)

      # Seleciona o seletor dos modelos
      self.driver.find_element(By.CSS_SELECTOR, selectors_html.model_selector).click()
      time.sleep(1)

      # Filtro do modelo desejado
      input = self.driver.find_element(By.CSS_SELECTOR, selectors_html.input_model_selector)
      input.send_keys(modelo_base)
      time.sleep(1)

      # Pega todos os filhos da <ul> de modelos
      ul_model_element = self.driver.find_element(By.CSS_SELECTOR, selectors_html.ul_model_selector)
      ul_model_element_children = ul_model_element.find_elements(By.XPATH, "./*")

      for index, item in enumerate(ul_model_element_children):
        models_names.append((index, item.text))
    
    return models_names

  # Web Scrapping
  def search_models(self, marca, modelo_base, mes_busca, ano_busca):
    self.setup()
    return self.get_models_from_model_base(marca, modelo_base, mes_busca, ano_busca)

  # Retornar lista dos modelos que possuem alguma palavra específica
  def return_models_with_an_especific_word(self, list_models, word):
    new_models = []
    for model in list_models:
      if model[1].count(word):
        new_models.append(model)
    
    return new_models

  # Retornar (True ou False) se for um número flutuante
  def is_float_number(self, value):
    if value.isdigit():
      return False
    return value.replace('.','',1).isdigit()

  # Retornar o número flutuante contido na string
  def return_float_number(self, string):
    list_strings = string.split(" ")

    for item in list_strings:
      if self.is_float_number(item):
        value = float(item)
        return value
    return None

  # Retornar lista com maior e menor motorização de marca e modelo_base
  def get_larger_and_smaller_vehicle(self, word, remove_list=[]):

    values_with_indexes = []
    new_models_names = self.return_models_with_an_especific_word(self.models_names, word)
    if len(new_models_names) == 0:
      new_models_names = self.return_models_with_an_especific_word(self.models_names, "")

    list_values = []
    for model in new_models_names:
      float_number = self.return_float_number(model[1])
      if float_number != None:
        list_values.append((model[0], float_number))

    if verbose:
      print("\nlist_values")
      util.print_formatted_json(list_values)

    # Itens que podem ser removidos da resposta de consulta (para não termos valores repetidos)
    for remove_item in remove_list:
      try:
        list_values.remove(remove_item)
      except:
        if verbose:
          print("Elemento não está na lista para ser removido!")

    if(len(list_values) > 1):
      maximum_value = max(list_values, key=lambda x:x[1])
      list_values.remove(maximum_value)
      minimum_value = min(list_values, key=lambda x:x[1])

      values_with_indexes.append(maximum_value)
      values_with_indexes.append(minimum_value)
    else:
      if verbose:
        print("Não há elementos suficientes na lista 'list_values'")
      values_with_indexes = list_values

    return values_with_indexes

  # Retornar lista de nomes dos modelos a partir da lista de indices
  def get_names_from_indexes(self, list_indexes, list_names):
    new_list_names = []
    indexes_not_repeated = []

    for item in list_indexes:
      if item[0] is not indexes_not_repeated:
        new_list_names.append(list_names[item[0]][1])
        indexes_not_repeated.append(item[0])

    return new_list_names

  # Fechar execução
  def close(self):
    self.driver.close()

  # filtro para os nomes dos modelos
  def filter_model_names(self, modelo_base):
    self.models_names = self.models_names

  # Execution
  def execution(self):
    
    self.models_names = self.get_models_from_model_base(
      self.marca,
      self.modelo_base,
      self.mes_busca,
      self.ano_busca
    )
    self.filter_model_names(self.modelo_base)

    if len(self.models_names):
      values_with_indexes = []
      for word in self.words:
        values_with_indexes += self.get_larger_and_smaller_vehicle(word, values_with_indexes)

      new_list_names = self.get_names_from_indexes(values_with_indexes, self.models_names)
      return new_list_names

    else:
      return []
