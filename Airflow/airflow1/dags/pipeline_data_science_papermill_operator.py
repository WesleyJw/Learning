from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow.utils.dates import days_ago
import random

args =  {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'description' : "A DAG de teste exemplificar a utilização do papermill integrado ao Airflow."    
}

#diretório padrão de dags.
dags_path = "/opt/airflow/dags/"

with DAG(dag_id="pipeline_data_science_papermill",
    default_args=args,
    schedule_interval=None
    ) as dag:

    run_notebook_task = PapermillOperator(
    task_id="run_example_notebook",
    input_nb= dags_path+'data-science-project/regression-project.ipynb',
    output_nb= dags_path+'data-science-project/output-{{ execution_date }}.ipynb',
    parameters={ 
                 "test_size_": 0.25
                ,"dataset" : dags_path+"data-science-project/data/ecomerce.csv"
                ,"model" : dags_path+"/data-science-project/model/"
   				,"n_estimators" : 1000
   				,"max_depth" : 5
            },
    )

run_notebook_task