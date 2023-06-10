from airflow import DAG
import airflow.utils.dates
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.utils.edgemodifier import Label


dag = DAG(
    dag_id="edge_labels",
    description="DAG de exemplo para exemplificar a funcionalidade de definir labels para as arestas",
    start_date=airflow.utils.dates.days_ago(14),
    schedule_interval=None,
)

def check_acuracy(ti):
    acuracy_value = int(ti.xcom_pull(key="model_acuracy"))
    if acuracy_value >= 90:
        return 'deploy_task'
    else:
        return 'retrain_task'

get_acuracy_op = BashOperator(
    task_id='get_acuracy_task',
    bash_command='echo "{{ ti.xcom_push(key="model_acuracy", value=90) }}"',
    dag=dag,
)

check_acuracy_op = BranchPythonOperator(
    task_id='check_acuracy_task',
    python_callable=check_acuracy,
    dag=dag,
)

deploy_op = DummyOperator(task_id='deploy_task', dag=dag)
retrain_op = DummyOperator(task_id='retrain_task', dag=dag)
notify_op = DummyOperator(task_id='notify_task', trigger_rule=TriggerRule.NONE_FAILED, dag=dag)

get_acuracy_op >> check_acuracy_op
check_acuracy_op >> Label("ACC >= 90%") >> deploy_op >> notify_op
check_acuracy_op >> Label("ACC < 90%") >> retrain_op >> notify_op