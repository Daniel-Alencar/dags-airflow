from airflow import DAG
import datetime as dt

from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

def message():
  print("O arquivo foi encontrado!")

# Executar de 30 em 30 segundos

with DAG('teste_interval_2', start_date = dt.datetime(2022,7,20),
         schedule_interval = dt.timedelta(seconds=60), catchup = False) as dag:
  
  wait_for_file = FileSensor(
    task_id = "wait_for_file",
    filepath = "/mnt/31f07ee3-e7ad-49de-a4d4-9295fa9b72ec/Arquivos/MEGA/Documents/Projetos pessoais/IC/airflow-test/file.csv",
    poke_interval = 20,  # seconds
    timeout = 45,  # seconds

    soft_fail = True, # Skip in case of failure
    mode = 'reschedule' 
  )

  messageTask = PythonOperator(
    task_id = 'messageTask',
    python_callable = message
  )

  wait_for_file >> messageTask