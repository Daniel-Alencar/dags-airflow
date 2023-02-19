import time
import util

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from settings import verbose, headless


ano = 2016

# Faz o Web-Scrapping para algum site
def web_scrapping():
  # Configuracoes do selenium
  option = Options()
  option.headless = headless
  driver = webdriver.Firefox(options=option)

  # Site onde sera o webscrapping
  url = "https://www.autoo.com.br/emplacamentos/"

  # Seletor da categoria
  category_selector = "#formRankCat > select"
  more_popular_selector = '#formRankCat > select:nth-child(1) > optgroup:nth-child(2)'
  more_popular_choosen_selector = '#formRankCat > select > optgroup:nth-child(2)'

  # Seletor do ano
  year_selector = "#selectCatRank > select"

  # Seletor da tabela com os veiculos e valores
  table_selector = "#example > tbody"

  # Carregar a pagina
  driver.get(url)
  time.sleep(2)

  # Verifica as categorias mais poulares
  more_popular_choosen = driver.find_element(By.CSS_SELECTOR, more_popular_choosen_selector)
  more_popular_choosen_children = more_popular_choosen.find_elements(By.XPATH, "./*")
  
  values = []

  for i in range(len(more_popular_choosen_children)):
    # Seleciona seletor da categoria 
    driver.find_element(By.CSS_SELECTOR, category_selector).click()

    # Seleciona categoria especifica
    more_popular_element_selector = f'{more_popular_selector} > option:nth-child({i + 1})'
    more_popular_element = driver.find_element(By.CSS_SELECTOR, more_popular_element_selector)
    category_name = more_popular_element.text
    more_popular_element.click()
    time.sleep(1)

    # Seleciona o ano especifico
    seletor_do_ano = driver.find_element(By.CSS_SELECTOR, year_selector)
    seletor_do_ano.click()

    seletor_do_ano_children = seletor_do_ano.find_elements(By.XPATH, "./*")

    for index, seletor_do_ano_child in enumerate(seletor_do_ano_children):
      if str(ano) == seletor_do_ano_child.text:

        driver.find_element(By.CSS_SELECTOR, f'{year_selector} > option:nth-child({index + 1})').click()
        time.sleep(2)
        break

    # Verifica os filhos da tabela
    table = driver.find_element(By.CSS_SELECTOR, table_selector)
    table_children = table.find_elements(By.XPATH, "./*")

    values.append({ category_name: [] })

    # Pega marca e modelo dos veiculos da tabela
    for j in range(len(table_children)):
      parity = "even" if (j % 2) else "odd"
      marca = f'tr.{parity}:nth-child({j + 1}) > td:nth-child(2) > a:nth-child(1) > span:nth-child(2)'
      modelo = f'tr.{parity}:nth-child({j + 1}) > td:nth-child(2) > a:nth-child(1) > span:nth-child(3)'
      values[i][category_name].append({
        'marca': driver.find_element(By.CSS_SELECTOR, marca).text,
        'modelo': driver.find_element(By.CSS_SELECTOR, modelo.lstrip()).text.strip()
      })

  # Encerra o selenium
  driver.quit()
  
  # Retorna o resultado
  return { "vehicles": values }

values = web_scrapping()
if verbose:
  print(values)

if verbose:
  util.print_formatted_json(values)

util.update_json(f"json/vehicles_{ano}.json", values)