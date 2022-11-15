from airflow import DAG
from datetime import datetime

from airflow.operators.python import PythonOperator

def hello():
  print("Hello world")

with DAG('teste0', start_date = datetime(2022,5,23),
         schedule_interval = '30 * * * *', catchup = False) as dag:
  
  helloWorld = PythonOperator(
    task_id = 'Hello_World',
    python_callable = hello
  )

  helloWorld