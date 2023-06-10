import pandas as pd
import sqlalchemy


def _load(path_temp_csv):

    #conectando a base de dados de oltp.
    engine_postgresql_olap = sqlalchemy.create_engine('postgresql://postgres:airflow@172.17.0.3:3254/employees')

    #selecionando os dados.
    dataset = pd.read_csv(path_temp_csv)

    #Dataset load into olap server.
    dataset.to_sql("employees_dataset",
                   engine_postgresql_olap,
                   if_exists="replace",
                   index=False)
