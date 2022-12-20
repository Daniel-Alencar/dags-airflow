from airflow import DAG
import datetime as dt
from airflow.operators.python import PythonOperator

import util
from MongoDBWeb import MongoDBWeb
from web_scrapping import Web_Scrapping
from settings import number_of_computers, computer_id, mini_batch
from settings import vehicles_to_search_path, vehicles_with_price_path

def get_vehicles_to_search():
  vehicles_to_search = util.read_json(vehicles_to_search_path)
  # print(vehicles_to_search)

  return vehicles_to_search

def get_indices_de_busca(task_instance):
  vehicles_to_search = task_instance.xcom_pull(task_ids = 'get_vehicles_to_search')
  vehicles_to_search_length = len(vehicles_to_search)
  # print(vehicles_to_search_length)

  bd = MongoDBWeb(vehicles_to_search_length, number_of_computers)
  indices_de_busca = bd.get_indexes(computer_id)
  # print(indices_de_busca)

  return indices_de_busca

def run_web_scrapping(task_instance):
  vehicles_to_search = task_instance.xcom_pull(task_ids = 'get_vehicles_to_search')
  indices_de_busca = task_instance.xcom_pull(task_ids = 'get_indices_de_busca')

  web = Web_Scrapping(
    indices_de_busca=indices_de_busca,
    vehicles_to_search=vehicles_to_search,
    computer_id=computer_id,
    number_of_computers=number_of_computers
  )
  web.get_vehicles_with_price()
  web.execution(mini_batch)

def save_BD():
  bd = MongoDBWeb()
  vehicles_with_price = util.read_json(vehicles_with_price_path)
  
  bd.persistent(vehicles_with_price)

def clean_vehicles_with_price():
  util.clear_json(vehicles_with_price_path)
  


dag = DAG(
  dag_id = "Execution_web_scrapping",
  start_date = dt.datetime(year=2022, month=11, day=1),
  end_date = dt.datetime(year=2022, month=12, day=31),
  schedule_interval = '0 9 * * *',
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'get_vehicles_to_search',
  python_callable = get_vehicles_to_search,
  dag = dag
)

task_2 = PythonOperator(
  task_id = 'get_indices_de_busca',
  python_callable = get_indices_de_busca,
  dag = dag
)

task_3 = PythonOperator(
  task_id = 'run_web_scrapping',
  python_callable = run_web_scrapping,
  dag = dag
)

task_4 = PythonOperator(
  task_id = 'save_BD',
  python_callable = save_BD,
  dag = dag
)

task_5 = PythonOperator(
  task_id = 'clean_vehicles_with_price',
  python_callable = clean_vehicles_with_price,
  dag = dag
)

task_1 >> task_2 >> task_3 >> task_4 >> task_5