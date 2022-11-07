from airflow import DAG
import datetime as dt

from airflow.operators.python import PythonOperator

def hello():
  print("Hello world")

# Executar de 30 em 30 segundos

with DAG('teste_interval_0', start_date = dt.datetime(2022,7,20),
         schedule_interval = dt.timedelta(seconds=30), catchup = False) as dag:
  
  helloWorld = PythonOperator(
    task_id = 'Hello_World',
    python_callable = hello
  )

  helloWorld