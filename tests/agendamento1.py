from airflow import DAG
import datetime as dt

dag = DAG(
  dag_id ='agendamento1',
  start_date = dt.datetime(2022,9,9),
  schedule_interval = '30 * * * *',
)
