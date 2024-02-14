######################################
# Resposta para o exercício
######################################

from datetime import datetime

from airflow.decorators import dag, task

# Definir os argumentos padrão para o DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
}


@dag(
    "inferencia_modelo_dag",
    default_args=default_args,
    description="DAG simples para inferencia de um modelo scikit-learn",
    catchup=False,  # Não voltar no tempo para executar tarefas
    schedule=None,
    start_date=datetime(2023, 11, 13),
    tags=["inferencia", "scikit-learn", "resposta"],
)
def dag_inferencia_modelo():
    @task.virtualenv(
        task_id="preprocessamento",
        requirements=["pandas"],
        system_site_packages=False,
    )
    def preprocessamento():
        """Essa função executa o preprocessamento dos dados.

        Returns:
            str: Caminho para o arquivo csv com os dados preprocessados
        """
        import pandas as pd

        df = pd.DataFrame(
            {"feature1": range(20), "feature2": range(20, 40), "target": range(40, 60)}
        )
        df["feature1"] = df["feature1"] * 2

        df.to_csv("/tmp/data_inf.csv", index=False)
        return "/tmp/data_inf.csv"

    @task.virtualenv(
        task_id="inferencia_modelo",
        requirements=["pandas", "scikit-learn", "joblib"],
        system_site_packages=False,
    )
    def inferencia(csv_path: str):
        """Essa função executa a inferencia com o modelo.

        Args:
            csv_path (str): Caminho para o arquivo csv com os dados preprocessados

        Returns:
            str: predicoes do modelo
        """
        import json

        import joblib
        import pandas as pd

        df = pd.read_csv(csv_path)

        # ler a ultima linha do registro para obter o modelo mais recente
        with open("/opt/airflow/models/registro.txt", "r") as fp:
            ultimo_modelo = json.loads(fp.readlines()[-1])

        hash_modelo = ultimo_modelo["hash_modelo"]
        data_treino = ultimo_modelo["data_treinamento"]

        print(f"Usando o modelo {hash_modelo} treinado em {data_treino}")

        # carregar o modelo
        model = joblib.load(f"/opt/airflow/models/model_{hash_modelo}.pkl")

        # fazer a inferencia
        df["target"] = model.predict(df[["feature1", "feature2"]])

        # retornar o resultado
        return df["target"].to_json()

    preprocessamento_op = preprocessamento()
    inferencia_op = inferencia(preprocessamento_op)


dag_inferencia_modelo()
