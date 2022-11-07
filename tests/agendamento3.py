from airflow import DAG
import datetime as dt

dag = DAG(
    dag_id = "agendamento3",
    schedule_interval = dt.timedelta(days=3),
    start_date = dt.datetime(year=2022, month=9, day=1),
    end_date = dt.datetime(year=2022, month=9, day=30),
)
