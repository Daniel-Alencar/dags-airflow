from airflow import DAG
from datetime import datetime

from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator 

import pandas as pd
import requests
import json

def captura_conta_dados():
    url = "https://api.github.com/users/Daniel-Alencar/repos"
    response = requests.get(url)
    df = pd.json_normalize(json.loads(response.content))

    quantidade = len(df.index)
    return quantidade

def isValido(task_instance):
    quantidade = task_instance.xcom_pull(task_ids = 'task_1')

    # Especifica a próxima task a ser realizada
    if (quantidade > 30):
      return 'task_3'
    return 'task_4'

with DAG('new_teste', start_date = datetime(2022,5,23),
         schedule_interval = '30 * * * *', catchup = False) as dag:
  # Task de execução de scripts python
  T1 = PythonOperator(
      task_id = 'task_1',
      python_callable = captura_conta_dados
  )

  # Task de execução de scripts python + Escolha da próxima task a ser realizada
  T2 = BranchPythonOperator(
      task_id = 'task_2',
      python_callable = isValido
  )

  # Task de execução de comando no terminal Bash
  T3 = BashOperator(
    task_id = 'task_3',
    bash_command = 'echo "Quantidade OK"'
  )

  # Task de execução de comando no terminal Bash
  T4 = BashOperator(
    task_id = 'task_4',
    bash_command = 'echo "Quantidade não OK"'
  )

  # Define a ordem de execução das tasks
  T1 >> T2 >> [T3, T4]