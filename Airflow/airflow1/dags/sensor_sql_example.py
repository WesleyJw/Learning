from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.sensors.sql_sensor import SqlSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd
import glob

dag = DAG(
    dag_id = "sensor_sql_example",
    description = "Uma dag utilizando o sensor do SQL para monitorar uma tabela.",
    start_date = days_ago(1),
)

check_table_data = SqlSensor( 
     task_id='sql_sensor_check'
    ,poke_interval=30
    ,timeout=180
    ,sql="SELECT COUNT(*) FROM employees.sales_temp;"
    ,conn_id='mysql_oltp'
    ,dag = dag
)

print_message = BashOperator(
    task_id = "print_message",
    bash_command = "echo A tabela contém dados.",
    dag = dag,
)

check_table_data >> print_message