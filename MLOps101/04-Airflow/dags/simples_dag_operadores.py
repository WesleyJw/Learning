from datetime import datetime

from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator

# Definir os argumentos padrão para o DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
}

# Lista de operadores: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html


@dag(
    "dag_simples_com_diferentes_operadores",
    default_args=default_args,
    description="DAG de exemplo operadores",
    catchup=False,  # Não voltar no tempo para executar tarefas
    schedule=None,
    start_date=datetime(2023, 11, 13),
    tags=["uma-tag-qualquer"],
)
def dag_simples_com_diferentes_operadores():
    python_operator = PythonOperator(
        task_id="python_operator",
        python_callable=lambda: print("Python Operator"),
    )
    bash_operator = BashOperator(
        task_id="bash_operator", bash_command="echo Bash Operator"
    )

    @task.virtualenv(
        task_id="tarefa_virtualenv",
        requirements=["pandas"],
        system_site_packages=False,  # Não usar as bibliotecas do sistema
    )
    def tarefa_virtualenv():
        import pandas as pd

        return "import pandas OK"

    def importar():
        import pandas as pd

        return "import pandas OK"

    operator_virtualenv_outro = PythonVirtualenvOperator(
        task_id="operator_virtualenv_outro",
        python_callable=importar,
        requirements=["pandas"],
        system_site_packages=False,  # Não usar as bibliotecas do sistema
    )

    # outra forma de definir a ordem das tarefas
    (
        python_operator
        >> bash_operator
        >> tarefa_virtualenv()
        >> operator_virtualenv_outro
    )


dag_simples_com_diferentes_operadores()
