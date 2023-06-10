from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id = "sensor_file_example",
    description = "Uma dag utilizando o sensor do tipo arquivo.",
    start_date = days_ago(1),
)

sensor_task = FileSensor( 
     task_id = "my_file_sensor_task"
    ,poke_interval = 30
    ,filepath = "/tmp/testfile.csv"
    ,dag = dag
    )

get_file_data = BashOperator(
    task_id = "get_file_data",
    bash_command = "cat /tmp/testfile.csv",
    dag = dag,
)

sensor_task >> get_file_data
