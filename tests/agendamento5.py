from airflow import DAG
import datetime as dt

from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def hello(date):
    print('Hello world!')
    print(date)

dag = DAG(
    dag_id = "agendamento5",
    schedule_interval = dt.timedelta(days=1),
    start_date = dt.datetime(year=2022, month=8, day=31),
    end_date = dt.datetime(year=2022, month=9, day=30),
    catchup = False
)

task_1 = PythonOperator(
    task_id = 'task_1',
    python_callable = hello,
    op_args = ['{{ ds }}'],
    dag = dag
)

task_2 = BashOperator(
    task_id="task_2",
    bash_command=(
        'echo "start_date={{ ds }} and end_date={{ next_ds }}"'
    )
)

task_1 >> task_2