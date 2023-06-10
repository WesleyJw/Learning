from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

path_stage = "/opt/airflow/dags/data/datasets/"

default_args = {
'start_date': datetime(2020, 1, 1)
}

def cross_validation(model,X,y):
    score = cross_val_score(model, X, y, cv=10)
    return score.mean()

def _load_transform():
    housing_df = pd.read_csv('/opt/airflow/dags/data/datasets/usa_housing.csv')

    X = housing_df[[  'Avg. Area Income'
                    , 'Avg. Area House Age'
                    , 'Avg. Area Number of Rooms'
                    , 'Avg. Area Number of Bedrooms'
                    , 'Area Population']]

    scaler = StandardScaler()
    
    X = scaler.fit_transform(X)
    y = housing_df['Price']

    np.savetxt(path_stage+"/X.csv", X, delimiter=",")
    np.savetxt(path_stage+"/y.csv", y, delimiter=",")

def train_linear_regression(ti):
    X = np.loadtxt(path_stage+"/X.csv", delimiter=",")
    y = np.loadtxt(path_stage+"/y.csv", delimiter=",")

    lin_reg = LinearRegression()
    score_mean = cross_validation(lin_reg, X, y)
    ti.xcom_push(key='model_r2', value=score_mean)

def train_random_forest_regression(ti):
    X = np.loadtxt(path_stage+"/X.csv", delimiter=",")
    y = np.loadtxt(path_stage+"/y.csv", delimiter=",")

    random_reg = RandomForestRegressor()
    score_mean = cross_validation(random_reg, X, y)
    ti.xcom_push(key='model_r2', value=score_mean)

def train_knn_regression(ti):
    X = np.loadtxt(path_stage+"/X.csv", delimiter=",")
    y = np.loadtxt(path_stage+"/y.csv", delimiter=",")
    
    knn_reg = KNeighborsRegressor()
    score_mean = cross_validation(knn_reg,X,y)
    ti.xcom_push(key='model_r2', value=score_mean)

def choose_best_model(ti):
    models = ["LinearRegression","RandomForestRegressor","KNeighborsRegressor"]
    
    r2_models = ti.xcom_pull(key='model_r2', task_ids=["train_linear_reg","train_random_reg","train_knn_reg"])
    index_best_model = r2_models.index(max(r2_models))
    
    print('Melhor modelo: {}, Score: {}'.format(models[index_best_model],r2_models[index_best_model]))


with DAG('xcom_example', schedule_interval='@daily', default_args=default_args) as dag:
    
    load_transform_task = PythonOperator(
        task_id = "load_transform",
        python_callable = _load_transform
    )

    train_linear_regression_task = PythonOperator(
        task_id = "train_linear_reg",
        python_callable = train_linear_regression
    )

    train_random_regression_task = PythonOperator(
        task_id = "train_random_reg",
        python_callable = train_random_forest_regression
    )

    train_knn_regression_task = PythonOperator(
        task_id = "train_knn_reg",
        python_callable = train_knn_regression
    )

    choose_best_model_task = PythonOperator(
        task_id = "choose_best_model",
        python_callable = choose_best_model
    )

load_transform_task >> [ train_linear_regression_task
                        ,train_random_regression_task
                        ,train_knn_regression_task
                    ] >> choose_best_model_task