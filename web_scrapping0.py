from airflow import DAG
import datetime as dt
from airflow.operators.python import PythonOperator


# Configura inicialmente o web_scrapping
def setup_web_scrapping():
  print("Hello world!")


dag = DAG(
  dag_id = "web_scrapping0",
  schedule_interval = dt.timedelta(days=1),
  start_date = dt.datetime(year=2022, month=11, day=5),
  end_date = dt.datetime(year=2022, month=11, day=10),
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'task_1',
  python_callable = setup_web_scrapping,
  dag = dag
)

task_1