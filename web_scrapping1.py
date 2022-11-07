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



# Configura inicialmente o web_scrapping
def setup_web_scrapping():
  print("Hello world!")


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

  driver.quit()


dag = DAG(
  dag_id = "web_scrapping1",
  schedule_interval = dt.timedelta(days=1),
  start_date = dt.datetime(year=2022, month=11, day=5),
  end_date = dt.datetime(year=2022, month=11, day=10),
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'task_1',
  python_callable = setup_web_scrapping,
  dag = dag
)

task_1