from datetime import datetime

from airflow.decorators import dag, task

# Definir os argumentos padrão para o DAG
args_padrao = {
    "owner": "airflow",
    "depends_on_past": False,
}


@dag(
    "treino_modelo_dag",
    default_args=args_padrao,
    description="DAG simples para treino de um modelo scikit-learn",
    catchup=False,  # Não voltar no tempo para executar tarefas
    schedule=None,  # None para desabilitar o agendamento e rodar apenas uma vez
    start_date=datetime(2023, 11, 13),
    tags=["treino", "scikit-learn"],
)
def dag_treinar_modelo():
    """DAG para treino de um modelo de ML"""

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

        df.to_csv("/tmp/data.csv", index=False)
        return "/tmp/data.csv"

    @task.virtualenv(
        task_id="treino_modelo",
        requirements=["pandas", "scikit-learn", "joblib"],
        system_site_packages=False,
    )
    def treino(csv_path: str):
        """Essa função executa o treino do modelo.

        Args:
            csv_path (str): Caminho para o arquivo csv com os dados preprocessados

        Returns:
            bool: True se o treino foi executado com sucesso
        """
        import json
        from datetime import datetime

        import joblib
        import pandas as pd
        from sklearn.linear_model import LinearRegression

        # read the csv file
        df = pd.read_csv(csv_path)

        X = df[["feature1", "feature2"]]
        y = df["target"]
        model = LinearRegression()
        model.fit(X, y)
        # criar um hash para o modelo
        hash_modelo = joblib.hash(model)

        # salvar modelo em /opt/airflow/models
        joblib.dump(model, f"/opt/airflow/models/model_{hash_modelo}.pkl")

        # criar um arquivo com o hash do modelo
        with open("/opt/airflow/models/registro.txt", "a") as f:
            f.write(
                json.dumps(
                    {
                        "hash_modelo": hash_modelo,
                        "data_treinamento": datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                    }
                )
            )
        return True

    preprocessamento_op = preprocessamento()
    treino_op = treino(preprocessamento_op)


dag_treinar_modelo()
