from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import random

args =  {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'description' : "A DAG de teste exemplificar o conceito de retries."    
}

def coleta_dados_web():
    n = random.random() 
    print("Número aleatório: {}".format(n))
    if n > 0.3:
       raise Exception("Erro aqui!")
    print("Coleta OK!")

def processa_dados():
    print("Inicia o processamento")

with DAG(dag_id="retries_example",
    default_args=args,
    schedule_interval=None
    ) as dag:

    coleta_dados_task = PythonOperator(
    task_id="coleta_dados",
    python_callable=coleta_dados_web,
    retries=10,
    retry_delay=timedelta(seconds=30)
    )

    process_dados_task = PythonOperator(
    task_id="processa_dados",
    python_callable=processa_dados
    )

coleta_dados_task >> process_dados_task