from airflow import DAG
import datetime as dt

dag = DAG(
  dag_id ='agendamento2',
  start_date = dt.datetime(2022,9,2),
  end_date = dt.datetime(2022,9,9),
  schedule_interval = '@daily',
)
