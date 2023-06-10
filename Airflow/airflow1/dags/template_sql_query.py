from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
import datetime as dt

with DAG(dag_id="templates_sql_query",
    description="A DAG de teste exemplificar a utilização de templates consultas sql",
    start_date=dt.datetime(2021, 7, 19),
    schedule_interval='@daily'
    ) as dag:
    
    drop_table_if_exist = MySqlOperator(
        task_id='drop_table_mysql', 
        mysql_conn_id='mysql_conn_oltp',
        sql="""
            DROP TABLE IF EXISTS sales_temp;
            """
    )

    create_table_mysql_task = MySqlOperator(
        task_id='create_table_mysql', 
        mysql_conn_id='mysql_conn_oltp',
        sql="""
            CREATE TABLE sales_temp AS
            SELECT * FROM sales
            WHERE DATA BETWEEN "{{ execution_date.strftime("%d/%m/%y") }}" AND "{{ execution_date.strftime("%d/%m/%y") }}";
            """
    )

    drop_table_if_exist >> create_table_mysql_task