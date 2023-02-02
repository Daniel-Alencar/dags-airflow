from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.taskinstance import clear_task_instances
from airflow.utils.db import provide_session

import datetime as dt

import util
from MongoDBWeb import MongoDBWeb
from web_scrapping import Web_Scrapping

from settings import number_of_computers, computer_id, verbose
from settings import incomplete_to_search_path, vehicles_with_price_path
from settings import retries, retry_delay, incomplete_path, modelo_atual_path

@provide_session
def retry_upstream_tasks(context, session = None, adr = False):
  task_ids_to_retry = []
  j, a_task = 0, context['task']

  while j < context['params']['retry_upstream_depth']:
    num_upstream_tasks = len(a_task.upstream_task_ids)
    if num_upstream_tasks != 1:
      raise ValueError(f'The # of upstream tasks of "{a_task}" must be 1, but "{num_upstream_tasks}"')
    upstream_task_id = list(a_task.upstream_task_ids)[0]
    task_ids_to_retry.append(upstream_task_id)
    upstream_task = [t for t in context['dag'].tasks if t.task_id == upstream_task_id][0]
    a_task = upstream_task
    j += 1

  all_task_ids_to_instances = {t_ins.task_id: t_ins for t_ins in context['dag_run'].get_task_instances()}
  task_instances_to_retry = [all_task_ids_to_instances[tid] for tid in task_ids_to_retry[::-1]]

  clear_task_instances(
    tis = task_instances_to_retry, 
    session = session, 
    activate_dag_runs = adr, 
    dag = context['dag']
  )

def get_vehicles_to_search():
  vehicles_to_search = util.read_json(incomplete_to_search_path)
  if verbose:
    print(vehicles_to_search)

  return vehicles_to_search

def get_indices_de_busca(task_instance):
  vehicles_to_search = task_instance.xcom_pull(task_ids = 'get_vehicles_to_search')
  vehicles_to_search_length = len(vehicles_to_search)

  bd = MongoDBWeb(vehicles_to_search_length, number_of_computers)
  indices_de_busca = bd.get_indexes(computer_id)
  if verbose:
    print(indices_de_busca)

  return indices_de_busca

def run_web_scrapping(task_instance):
  vehicles_to_search = task_instance.xcom_pull(task_ids = 'get_vehicles_to_search')
  indices_de_busca = task_instance.xcom_pull(task_ids = 'get_indices_de_busca')

  bd = MongoDBWeb()
  indexes = bd.get_indexes(computer_id)

  # Pegar o elemento de incomplete.json e passar para modelo atual
  incomplete = util.read_json(incomplete_path)
  util.update_json(modelo_atual_path, incomplete[indexes["marca"]])

  web = Web_Scrapping(
    indices_de_busca=indices_de_busca,
    vehicles_to_search=vehicles_to_search,
    computer_id=computer_id,
    number_of_computers=number_of_computers
  )
  web.get_vehicles_with_price()
  web.execution(mini_batch=1)

def save_BD():
  bd = MongoDBWeb()
  vehicles_with_price = util.read_json(vehicles_with_price_path)
  
  bd.persistent(vehicles_with_price)

def clear_vehicles_with_price():
  util.clear_json(vehicles_with_price_path)


dag = DAG(
  dag_id = "Execution_corrigir_modelos",
  start_date = dt.datetime(year=2023, month=1, day=27),
  end_date = dt.datetime(year=2023, month=12, day=31),
  schedule_interval = dt.timedelta(minutes=20),
  catchup = False
)

task_1 = PythonOperator(
  task_id = 'get_vehicles_to_search',
  python_callable = get_vehicles_to_search,
  dag = dag
)

task_2 = PythonOperator(
  task_id = 'get_indices_de_busca',
  python_callable = get_indices_de_busca,
  dag = dag
)

task_3 = PythonOperator(
  task_id = 'run_web_scrapping',
  python_callable = run_web_scrapping,
  dag = dag,
  on_retry_callback = retry_upstream_tasks,
  retries = retries,
  params = {'retry_upstream_depth': 2},
  retry_delay = retry_delay
)

task_4 = PythonOperator(
  task_id = 'save_BD',
  python_callable = save_BD,
  dag = dag
)

task_5 = PythonOperator(
  task_id = 'clear_vehicles_with_price',
  python_callable = clear_vehicles_with_price,
  dag = dag
)

task_1 >> task_2 >> task_3 >> task_4 >> task_5