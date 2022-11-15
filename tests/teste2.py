from airflow import DAG
import datetime as dt
from airflow.operators.python import PythonOperator

def function1():
  obj = "String"
  
  return obj

def function2(task_instance):
  obj = task_instance.xcom_pull(task_ids = 'task_1')
  print(obj)




dag = DAG(
  dag_id = "teste2",
  start_date = dt.datetime(year=2022, month=11, day=5),
  end_date = dt.datetime(year=2022, month=11, day=20),
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'task_1',
  python_callable = function1,
  dag = dag
)

task_2 = PythonOperator(
  task_id = 'task_2',
  python_callable = function2,
  dag = dag
)

task_1 >> task_2