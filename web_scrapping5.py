from airflow import DAG
import datetime as dt
from airflow.operators.python import PythonOperator

from web_scrapping import Web_Scrapping

# Faz a execução do Web Scrapping de acordo com o que desejamos
web = Web_Scrapping()

dag = DAG(
  dag_id = "web_scrapping5",
  start_date = dt.datetime(year=2022, month=11, day=5),
  end_date = dt.datetime(year=2022, month=11, day=10),
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'task_1',
  python_callable = web.get_vehicles_to_search,
  dag = dag
)

task_2 = PythonOperator(
  task_id = 'task_2',
  python_callable = web.get_vehicles_with_price,
  dag = dag
)

task_3 = PythonOperator(
  task_id = 'task_3',
  python_callable = web.get_indices_de_busca,
  dag = dag
)

task_4 = PythonOperator(
  task_id = 'task_4',
  python_callable = web.execution,
  dag = dag
)

task_1 >> task_2 >> task_3 >> task_4