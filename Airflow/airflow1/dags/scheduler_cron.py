from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="scheduler-cron",
    description="A DAG de teste para agendamento cron-based no Airflow",
    schedule_interval="15 23 * * *",
    start_date=datetime(2021, 7, 25),
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
