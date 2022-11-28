from airflow import DAG
import datetime as dt
from airflow.operators.python import PythonOperator

from web_scrapping import Web_Scrapping

web = None
def create_web_scrapping():
  global web
  web = Web_Scrapping()

def update_parameters():
  global web
  web.get_vehicles_to_search()
  web.get_vehicles_with_price()
  web.get_indices_de_busca()

def execute_web_scrapping():
  global web
  web.execution()




dag = DAG(
  dag_id = "web_scrapping3",
  start_date = dt.datetime(year=2022, month=11, day=5),
  end_date = dt.datetime(year=2022, month=11, day=10),
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'task_1',
  python_callable = create_web_scrapping,
  dag = dag
)

task_2 = PythonOperator(
  task_id = 'task_2',
  python_callable = update_parameters,
  dag = dag
)

task_3 = PythonOperator(
  task_id = 'task_3',
  python_callable = execute_web_scrapping,
  dag = dag
)

task_1 >> task_2 >> task_3