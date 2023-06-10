from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python import PythonOperator
import pandas as pd
import sqlalchemy

path_temp_csv = "/tmp/dataset.csv"
email_failed = "felipesf05@gmail.com"

dag = DAG(
    dag_id="elt-pipeline1",
    description="Pipeline para o processo de ETL dos ambientes de produção oltp ao olap.",
    start_date=days_ago(2),
    schedule_interval=None,
)

def _extract():
    #conectando a base de dados de oltp.
    engine_mysql_oltp = sqlalchemy.create_engine('mysql+pymysql://root:airflow@172.17.0.2:3306/employees')
    
    #selecionando os dados.
    dataset_df = pd.read_sql_query(r"""
                        SELECT   emp.emp_no
                        , emp.first_name
                        , emp.last_name
                        , sal.salary
                        , titles.title 
                        FROM employees emp 
                        INNER JOIN (SELECT emp_no, MAX(salary) as salary 
                                    FROM salaries GROUP BY emp_no) 
                        sal ON sal.emp_no = emp.emp_no 
                        INNER JOIN titles 
                        ON titles.emp_no = emp.emp_no
                        LIMIT 1000"""
                        ,engine_mysql_oltp
    )
    #exportando os dados para a área de stage.
    dataset_df.to_csv(
        path_temp_csv,
        index=False
    )

def _transform():
    
    dataset_df = pd.read_csv(path_temp_csv)

    #transformando os dados dos atributos.
    dataset_df["name"] = dataset_df["first_name"]+" "+dataset_df["last_name"]
    
    dataset_df.drop([    "emp_no"
                        ,"first_name"
                        ,"last_name"
                    ]
                    ,axis=1
                    ,inplace=True)
    
    #persistindo o dataset no arquivo temporario.
    dataset_df.to_csv(
        path_temp_csv,
        index=False
    )

def _load():
    #conectando com o banco de dados postgresql
    engine_postgresql_olap = sqlalchemy.create_engine('postgres+psycopg2://postgres:airflow@172.17.0.3:5432/employees')
    
    #selecionando os dados.
    #lendo os dados a partir dos arquivos csv.
    dataset_df = pd.read_csv(path_temp_csv)

    #carregando os dados no banco de dados.
    dataset_df.to_sql("employees_dataset", engine_postgresql_olap, if_exists="replace",index=False)

extract_task = PythonOperator(
    task_id="Extract_Dataset", 
    python_callable=_extract,
    email_on_failure=True,
    email=email_failed, 
    dag=dag
)

transform_task = PythonOperator(
    task_id="Transform_Dataset",
    email_on_failure=True,
    email=email_failed, 
    python_callable=_transform, 
    dag=dag
)

load_task = PythonOperator(
    task_id="Load_Dataset",
    email_on_failure=True,
    email=email_failed, 
    python_callable=_load,
    dag=dag
)

clean_task = BashOperator(
    task_id="Clean",
    email_on_failure=True,
    email=email_failed,
    bash_command="scripts/clean.sh",
    dag=dag
)

email_task = EmailOperator(
    task_id="Notify",
    email_on_failure=True,
    email=email_failed, 
    to='felipesf05@gmail.com',
    subject='Pipeline Finalizado',
    html_content='<p> O Pipeline para atualização de dados entre os ambientes OLTP e OLAP foi finalizado com sucesso. <p>',
    dag=dag)

extract_task >> transform_task >> load_task >> clean_task >> email_task
