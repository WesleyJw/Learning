import pandas as pd
import sqlalchemy


def _extract(path_temp_csv):

    #conectando a base de dados de oltp.
    engine_mysql_oltp = sqlalchemy.create_engine('postgresql://postgres:airflow@172.17.0.3:3254/oltp')

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
