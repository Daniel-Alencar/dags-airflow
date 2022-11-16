from airflow import DAG
import datetime as dt
from airflow.operators.python import PythonOperator

from web_scrapping import Web_Scrapping

# Faz a execução do Web Scrapping de acordo com o que desejamos
def execution():
  web = Web_Scrapping()
  web.get_vehicles_to_search()
  web.get_vehicles_with_price()
  web.get_indices_de_busca()
  web.execution()

dag = DAG(
  dag_id = "web_scrapping5",
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