from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd
import glob

dag = DAG(
    dag_id = "sensor_folder_example",
    description = "Uma dag utilizando o sensor do tipo arquivo para monitorar um diretório.",
    start_date = days_ago(1),
)

def processing_files_csv():
    # Empty DataFrame
    df_people = pd.DataFrame()

    # Concat files with DataFrame
    for file_name in glob.glob('/tmp/data_lake/*.json'):
        _df = pd.read_json(file_name)
        print("Concating file {}".format(file_name))
        df_people = pd.concat([df_people, _df])
    
    # Export data to csv
    df_people.to_csv("/tmp/data_lake/people.csv",index=False)


check_folder = FileSensor( 
     task_id = "check_folder_export"
    ,poke_interval = 30
    ,filepath = "/tmp/export_data"
    ,dag = dag
    )

move_files_to_data_lake = BashOperator(
    task_id = "move_files_to_dl",
    bash_command = "mv /tmp/export_data/*.* /tmp/data_lake/",
    dag = dag,
)

processing_files_export = PythonOperator(
    task_id="processing_files_export_csv", 
    python_callable=processing_files_csv,
    dag=dag
)

clean_json_files = BashOperator(
    task_id = "clean_json_files",
    bash_command = "rm -f /tmp/data_lake/*.json",
    dag = dag,
)

check_folder >> move_files_to_data_lake >> processing_files_export >> clean_json_files