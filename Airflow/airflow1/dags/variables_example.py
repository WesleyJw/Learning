from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

with DAG(dag_id="variables_example",
    description="A DAG de teste exemplificar a utilização de variáveis.",
    start_date=dt.datetime(2021, 7, 19),
    schedule_interval=None
    ) as dag:

    t1 = BashOperator(
    task_id="t1",
    bash_command="echo {{ var.value.volume_temp }}",
    )

t1