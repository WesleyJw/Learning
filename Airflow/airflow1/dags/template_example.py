from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

with DAG(dag_id="template_example",
    description="A DAG de teste exemplificar a utilização de templates.",
    start_date=dt.datetime(2021, 7, 19),
    schedule_interval=None
    ) as dag:
    
    t1 = BashOperator(
    task_id="t1",
    bash_command="echo Data de execução: {{ execution_date }}",
    )

    t2 = BashOperator(
    task_id="t2",
    bash_command='echo Data de execução formatada: {{ execution_date.strftime("%d/%m/%Y") }}',
    )
   
    t1 >> t2