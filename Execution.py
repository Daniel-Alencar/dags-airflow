from airflow import DAG
import datetime as dt
from airflow.operators.python import PythonOperator

import util
from MongoDBWeb import MongoDBWeb
from web_scrapping import Web_Scrapping

def get_indices_de_busca():
  bd = MongoDBWeb()
  indices_de_busca = bd.get_indexes()

  return indices_de_busca

def get_vehicles_to_search():
  vehicles_to_search = util.read_json("/home/engenheiro/airflow/dags/json/vehicles_to_search.json")

  return vehicles_to_search

def run_web_scrapping(task_instance):
  indices_de_busca = task_instance.xcom_pull(task_ids = 'task_1')
  vehicles_to_search = task_instance.xcom_pull(task_ids = 'task_2')

  web = Web_Scrapping(indices_de_busca, vehicles_to_search)
  web.get_vehicles_with_price()

  # Salva no arquivo vehicles_with_price.json
  web.execution()

def save_BD():
  bd = MongoDBWeb()
  bd.persistent("/home/engenheiro/airflow/dags/json/vehicles_with_price.json")



dag = DAG(
  dag_id = "web_scrapping8",
  start_date = dt.datetime(year=2022, month=11, day=5),
  end_date = dt.datetime(year=2022, month=11, day=20),
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'get_indices_de_busca',
  python_callable = get_indices_de_busca,
  dag = dag
)

task_2 = PythonOperator(
  task_id = 'get_vehicles_to_search',
  python_callable = get_vehicles_to_search,
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

[task_1, task_2] >> task_3 >> task_4