from datetime import datetime
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor

default_args = {
  'owner': 'Tiago Xavier',
  'depends_on_past': False
}

dag = DAG(
  'users-dag-raw',
  default_args=default_args,
  start_date=datetime.now(),
  schedule_interval='@daily',
  tags=['kubernetes', 'raw']
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

finish = DummyOperator(
    task_id='finish',
    dag=dag,
)

users_bronze_table = SparkKubernetesOperator(
  task_id ='users_raw',
  namespace ='processing',
  application_file='users.yaml',
  kubernetes_conn_id='kubernetes_in_cluster',
  do_xcom_push=True,
  dag=dag
)

monitor_users = SparkKubernetesSensor(
  task_id='monitor_users',
  namespace='processing',
  application_name="{{ task_instance.xcom_pull(task_ids='users_raw')['metadata']['name'] }}",
  kubernetes_conn_id='kubernetes_in_cluster',
  dag=dag
)


start >> users_bronze_table >> monitor_users >> finish