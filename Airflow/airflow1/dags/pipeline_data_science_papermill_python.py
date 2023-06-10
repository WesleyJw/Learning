import papermill as pm
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

args =  {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'description' : "A DAG de teste exemplificar a utilização do papermill através da sua API para Python."    
}

#diretório padrão de dags.
dags_path = "/opt/airflow/dags/"

def notebook_exec(**kwargs):
   pm.execute_notebook(
   kwargs['input_notebook'],
   kwargs['output'],
   parameters = dict( test_size_ = 0.25
   					, dataset = dags_path+"data-science-project/data/ecomerce.csv"
   					, model = dags_path+"data-science-project/model/"
   					, n_estimators = 1000
   					, max_depth = 5
   				)
)

with DAG(dag_id="pipeline_data_science_papermill_python",
    default_args=args,
    schedule_interval=None
    ) as dag:
    
    run_notebook_task = PythonOperator(
    task_id="run_notebook",
    python_callable=notebook_exec,
    op_kwargs={   
                'input_notebook': dags_path+'data-science-project/regression-project.ipynb'
               ,'output': dags_path+'data-science-project/output-{{ execution_date }}.ipynb'
            }
    )

run_notebook_task