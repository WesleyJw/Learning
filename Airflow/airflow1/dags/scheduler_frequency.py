import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="scheduler-frequency",
    description="A DAG de teste para agendamento frenquency based no Airflow",
    schedule_interval=dt.timedelta(minutes=5),
    start_date=dt.datetime(2021, 7, 25),
)

print_date_task = BashOperator(
    task_id="print_date",
    bash_command=(
        "echo Iniciando a tarefa: &&"
        "date"
    ),
    dag=dag,
)

processing_task = BashOperator(
    task_id="processing_data",
    bash_command=(
        "echo Processando os dados... &&"
        "sleep 50"
    ),
    dag=dag,
)

print_date_task >> processing_task
