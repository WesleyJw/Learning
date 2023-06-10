from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python import PythonOperator
import pandas as pd
from employees_etl.extract import _extract
from employees_etl.transform import _transform
from employees_etl.load import _load

path_temp_csv = "/tmp/dataset.csv"
email_failed = "jwesleybiologo@gmail.com"

# Create a Dag
dag = DAG(
    dag_id="etl-pipeline-employees",
    description="Pipeline to ETL process from OLTP environment to OLAP service",
    start_date=days_ago(2),
    schedule_interval="@daily"
)

# Operator Declarations
# Tasks definitions
extract_task = PythonOperator(
    task_id="Extract_Data_Employees",
    python_callable=_extract(path_temp_csv),
    email_on_failure=True,
    email=email_failed,
    dag=dag
)

# Tasks definitions
transform_task = PythonOperator(
    task_id="Transform_Data_Employees",
    python_callable=_transform(path_temp_csv),
    email_on_failure=True,
    email=email_failed,
    dag=dag
)

# Tasks definitions
load_task = PythonOperator(
    task_id="Load_Data_Employees",
    python_callable=_load(path_temp_csv),
    email_on_failure=True,
    email=email_failed,
    dag=dag
)

# Clean task to csv files
clean_task = BashOperator(
    task_id="Clean_Tmp_Employes",
    bash_command="scripts/clean.sh",
    email_on_failure=True,
    email=email_failed,
    dag=dag
)

# Task to send emails
email_task = EmailOperator(
    task_id="Notify",
    email_on_failure=True,
    email=email_failed, 
    to='wesley.datascientist@gmail.com',
    subject='Ended Pipeline',
    html_content='<p> The Pipeline to Data updated from OLTP service to OLAP service was ended with succsses. <p>',
    dag=dag
)

extract_task >> transform_task >> load_task >> clean_task >> email_task
