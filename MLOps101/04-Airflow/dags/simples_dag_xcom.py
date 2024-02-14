from datetime import datetime, timedelta

from airflow.operators.python_operator import PythonOperator

from airflow import DAG

# Maneira antiga de trabalhar com Xcom - dependencias entre tarefas.

# Função que será executada pela primeira tarefa
def task1_func(**kwargs):
    # Dados a serem compartilhados
    data_to_share = "Este é um dado compartilhado!"

    # XCom push para compartilhar dados com outras tarefas
    kwargs["ti"].xcom_push(key="shared_data_key", value=data_to_share)
    print("Task 1 executada. Dados compartilhados.")


# Função que será executada pela segunda tarefa
def task2_func(**kwargs):
    # XCom pull para recuperar dados compartilhados
    ti = kwargs["ti"]
    pulled_data = ti.xcom_pull(task_ids="task1", key="shared_data_key")
    print("Task 2 executada. Dados compartilhados recebidos:", pulled_data)


# Definição do DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
}

dag = DAG(
    "exemplo_dag_com_xcom",
    default_args=default_args,
    description="Um exemplo simples de DAG com XCom",
    schedule=None,
    start_date=datetime(2023, 11, 13),
)

# Tarefa 1
task1 = PythonOperator(
    task_id="task1",
    python_callable=task1_func,
    provide_context=True,
    dag=dag,
)

# Tarefa 2
task2 = PythonOperator(
    task_id="task2",
    python_callable=task2_func,
    provide_context=True,
    dag=dag,
)

# Definição das dependências entre as tarefas
task1 >> task2
