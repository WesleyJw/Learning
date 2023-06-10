from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

with DAG(dag_id="template_bash_operator",
    description="A DAG de teste exemplificar a utilização de templates em um script .sh",
    start_date=dt.datetime(2021, 7, 19),
    schedule_interval=None
    ) as dag:
    
    execute_script = BashOperator(
    task_id="execute_script",
    bash_command="/scripts/test.sh",
    env={'execution_date':'{{ ds }}'}
    )
   
    execute_script