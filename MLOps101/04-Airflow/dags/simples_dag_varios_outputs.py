from datetime import datetime

from airflow.decorators import dag, task

# Definir os argumentos padrão para o DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
}


@dag(
    "dag_simples_com_varios_outputs",
    default_args=default_args,
    description="DAG de exemplo",
    catchup=False,  # Não voltar no tempo para executar tarefas
    schedule=None,
    start_date=datetime(2023, 11, 13),
    tags=["uma-tag-qualquer"],
)
def dag_simples_com_varios_outputs():
    @task(multiple_outputs=True)
    def tarefa_1():
        return {
            "output_1": "valor de retorno da task 1",
            "output_2": "outro valor de retorno da task 1",
        }

    @task
    def tarefa_2(output_1: str, output_2: str):
        print(f"Task 2 recebeu {output_1} e {output_2}")
        print("Task 2")

    t1 = tarefa_1()
    tarefa_2(t1["output_1"], t1["output_2"])


dag_simples_com_varios_outputs()
