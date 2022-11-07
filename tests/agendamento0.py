from airflow import DAG
import datetime as dt

dag = DAG(
  dag_id ='agendamento0',
  start_date = dt.datetime(2022,9,2),
  schedule_interval = '@daily',
)
