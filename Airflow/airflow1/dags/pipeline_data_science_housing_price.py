import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago

args =  {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'description' : "Uma DAG para a automatização de um projeto de Data Science utilizando o Airflow."    
}

# diretório padrão de dags.
dags_path = "/opt/airflow/dags"

# área de staging.
staging_area = Variable.get("staging_area")
engineering_team = Variable.get("email_engineering_team")
science_team = Variable.get("email_science_team")


def _load_dataset_properties_to_staging():

    # carrega os dados de propriedades a partir do disco.
    df_ = pd.read_csv(dags_path+"/data/datasets/zillow/properties_2016.csv"
                ,nrows=10000
            )
    
    # persiste os arquivos na área de Staging.
    df_.to_parquet(  
                 staging_area+"/properties_2016.parquet"
                ,index = False
            )

def _load_dataset_train_to_staging():
    # carrega os dados de treinamento a partir do disco.
    df_ = pd.read_csv(dags_path+"/data/datasets/zillow/train_2016_v2.csv"
                ,nrows=10000
    )
    
    # persiste os arquivos no formato parquet na área de Staging.
    df_.to_parquet(  
                 staging_area+"/train_2016_v2.parquet"
                ,index = False
            )

def _join_datasets():
    # carrega os dados de propriedades e train a partir da área de staging.
    df_properties = pd.read_parquet(staging_area+"/properties_2016.parquet")
    df_train = pd.read_parquet(staging_area+"/train_2016_v2.parquet")
    
    # realiza o merge dos datasets através do id.
    df_final = df_properties.copy()
    df_final = df_final.merge(df_train, how = 'inner', on = 'parcelid')

    # persiste o dataset final para a área de staging.
    df_final.to_parquet(  
                 staging_area+"/zillow_dataset.parquet"
                ,index = False
            )

def _check_remove_duplicated_rows():
    # carrega o dataset partir da área de staging.
    df_zillow = pd.read_parquet(staging_area+"/zillow_dataset.parquet")
    
    # remove registros duplicados do atributo id.
    df_zillow.drop_duplicates(
                  subset = "parcelid"
                , keep = "first"
                , inplace = True
            )
    
    # persiste o dataset final para a área de staging.
    df_zillow.to_parquet(  
                 staging_area+"/zillow_dataset.parquet"
                ,index = False
            )

def _drop_columns_percent_missing_values(**kwargs):
    # carrega o dataset partir da área de staging.
    df_zillow = pd.read_parquet(staging_area+"/zillow_dataset.parquet")

    percent_limit = kwargs['percent_limit']

    # retornando as variáveis que contém pelo menos 1 registro missing.
    missing_var = [var for var in df_zillow.columns if df_zillow[var].isnull().sum() > 0]

    # definindo o percentual limite de registros nulos
    limit = np.abs((df_zillow.shape[0] * percent_limit))
    
    # selecionando apenas as variaveis que contém registros nulos superiores ao limite. 
    columns_drop = [var for var in missing_var if df_zillow[var].isnull().sum() > limit]
    
    # removendo as variáveis selecionadas.
    df_zillow.drop(columns=columns_drop, axis=1, inplace=True)

    # persiste o dataset final para a área de staging.
    df_zillow.to_parquet(  
                 staging_area+"/zillow_dataset.parquet"
                ,index = False
            )

def _transform_rescale_features():
    # carrega o dataset partir da área de staging.
    df_zillow = pd.read_parquet(staging_area+"/zillow_dataset.parquet")

    # gerando a feature elapsed time.
    df_zillow['yeardifference'] = df_zillow['assessmentyear'] - df_zillow['yearbuilt']

    # retornando as features para a escala original.
    df_zillow[['latitude', 'longitude']] = (df_zillow[['latitude', 'longitude']])/(10**6)
    df_zillow['censustractandblock'] = (df_zillow['censustractandblock'])/(10**12)
    df_zillow['rawcensustractandblock'] = (df_zillow['rawcensustractandblock'])/(10**6)

    # excluindo as features transformadas.
    df_zillow.drop(columns=['assessmentyear', 'yearbuilt', 'transactiondate'], axis=1, inplace=True)

    # persiste o dataset final para a área de staging.
    df_zillow.to_parquet(  
                 staging_area+"/zillow_dataset.parquet"
                ,index = False
            )

def _fill_missing_values():
    # carrega o dataset partir da área de staging.
    df_zillow = pd.read_parquet(staging_area+"/zillow_dataset.parquet")

    # retornando as variáveis que contém pelo menos 1 registro missing.
    missing_var = [var for var in df_zillow.columns if df_zillow[var].isnull().sum() > 0]

    # preenchendo os registros missing de cada variável pelo valor da moda.
    for var in missing_var:
        df_zillow[var] = df_zillow[var].fillna(df_zillow[var].mode()[0])

    # persiste o dataset final para a área de staging.
    df_zillow.to_parquet(  
                 staging_area+"/zillow_dataset.parquet"
                ,index = False
            )

def _encode_categorical_valiables():
    # carrega o dataset partir da área de staging.
    df_zillow = pd.read_parquet(staging_area+"/zillow_dataset.parquet")
    
    # seleciona apenas as variáveis do tipo categórico.
    categorical_variables = [var for var in df_zillow.columns if df_zillow[var].dtypes=='O']

    # realiza o enconding para cada variável.
    for i in range(len(categorical_variables)):
        # seleciona a variável a partir da lista.
        var = categorical_variables[i]
        
        # instancia o enconding.
        encoder = LabelEncoder()
        
        # gera os encodings.
        var_labels = encoder.fit_transform(df_zillow[var])
        var_mappings = {index: label for index, label in enumerate(encoder.classes_)}
        
        # atribui a nova variável ao dataset.
        df_zillow[(var + '_labels')] = var_labels
        
        # exclui a variável original.
        df_zillow.drop(columns=var, axis=1, inplace=True)

    # persiste o dataset final para a área de staging.
    df_zillow.to_parquet(  
                 staging_area+"/zillow_dataset.parquet"
                ,index = False
            )

def _drop_repetitive_useless_data():
    # carrega o dataset partir da área de staging.
    df_zillow = pd.read_parquet(staging_area+"/zillow_dataset.parquet")
    
    # excluindo variáveis desnecessárias.
    df_zillow.drop(   
                 columns=['censustractandblock'
                         ,'propertycountylandusecode_labels'
                         ,'parcelid']
                ,axis=1
                ,inplace=True
            )
    
    # persiste o dataset final para a área de staging.
    df_zillow.to_parquet(  
                 staging_area+"/zillow_dataset.parquet"
                ,index = False
            )

def _preprocessing_separate_train_test():
    # carrega o dataset partir da área de staging.
    df_zillow = pd.read_parquet(staging_area+"/zillow_dataset.parquet")

    # separa os conjuntos em X e Y.
    X = df_zillow.drop('logerror', axis=1)
    y = df_zillow['logerror']

    X_train, X_test, y_train, y_test = train_test_split(
                                     X
                                    ,y
                                    ,test_size = 0.25
                                    ,random_state = 100
                                )
    # seleciona as variáveis para aplicar o scaler.
    train_vars = [var for var in X_train.columns]

    # instancia e treina o scaler.
    scaler = StandardScaler()
    scaler.fit(X_train[train_vars]) 

    # aplica o scaler nos conjuntos de treino e test.
    X_train[train_vars] = scaler.transform(X_train[train_vars])
    X_test[train_vars] = scaler.transform(X_test[train_vars])

    # persiste os arquivos na área de staging.
    np.savetxt(staging_area+"/zillow_xtrain.csv", X_train, delimiter=",")
    np.savetxt(staging_area+"/zillow_ytrain.csv", y_train, delimiter=",")
    np.savetxt(staging_area+"/zillow_xtest.csv", X_test, delimiter=",")
    np.savetxt(staging_area+"/zillow_ytest.csv", y_test, delimiter=",")

def load_files_train_test_from_staging():
    # carregando os dados a partir da área de staging
    X_train = np.loadtxt(staging_area+"/zillow_xtrain.csv", delimiter=",")
    y_train = np.loadtxt(staging_area+"/zillow_ytrain.csv", delimiter=",")
    X_test = np.loadtxt(staging_area+"/zillow_xtest.csv", delimiter=",")
    y_test = np.loadtxt(staging_area+"/zillow_ytest.csv", delimiter=",")

    return X_train, y_train, X_test, y_test

def train_model(estimator, X_train, y_train, X_test, y_test):
    
    # treina o modelo.
    estimator.fit(X_train, y_train)

    # gera as predições.
    estimator_pred = estimator.predict(X_test)
    
    # calcula o erro absoluto médio.
    mean_abs_error = mean_absolute_error(y_test, estimator_pred)
    print('Mean Absolute Error : {}'.format(mean_abs_error))

    return mean_abs_error

def _train_model_regression_linear(ti):
    # carregando os dados a partir da área de staging
    X_train, y_train, X_test, y_test = load_files_train_test_from_staging()
    
    # instancia o algoritmo Regressão Linear.
    linear_reg = LinearRegression()

    # treina o modelo.
    mean_abs_error = train_model(linear_reg, X_train, y_train, X_test, y_test)

    # enviando as métricas para os metadados do Airflow.
    ti.xcom_push(key='mean_abs_error', value=mean_abs_error)

def _train_model_ada_boost_regressor(ti):
    # carregando os dados a partir da área de staging
    X_train, y_train, X_test, y_test = load_files_train_test_from_staging()
    
    # instancia o algoritmo Ada Boosting.
    adaboost_reg = AdaBoostRegressor()

    # treina o modelo.
    mean_abs_error = train_model(adaboost_reg, X_train, y_train, X_test, y_test)

    # enviando as métricas para os metadados do Airflow.
    ti.xcom_push(key='mean_abs_error', value=mean_abs_error)

def _train_model_gradient_boosting_regression(ti):
    # carregando os dados a partir da área de staging
    X_train, y_train, X_test, y_test = load_files_train_test_from_staging()
    
    # instancia o algoritmo Gradient Boosting.
    gb_reg = GradientBoostingRegressor()

    # treina o modelo.
    mean_abs_error = train_model(gb_reg, X_train, y_train, X_test, y_test)

    # enviando as métricas para os metadados do Airflow.
    ti.xcom_push(key='mean_abs_error', value=mean_abs_error)

def _train_model_decision_tree_regressor(ti):
    # carregando os dados a partir da área de staging
    X_train, y_train, X_test, y_test = load_files_train_test_from_staging()
    
    # instancia o algoritmo Decision Tree Regressor.
    tree_reg = DecisionTreeRegressor()

    # treina o modelo.
    mean_abs_error = train_model(tree_reg, X_train, y_train, X_test, y_test)

    # enviando as métricas para os metadados do Airflow.
    ti.xcom_push(key='mean_abs_error', value=mean_abs_error)

def _train_model_random_forest_regressor(ti):
    # carregando os dados a partir da área de staging
    X_train, y_train, X_test, y_test = load_files_train_test_from_staging()
    
    forest_reg = RandomForestRegressor()

    # treina o modelo.
    mean_abs_error = train_model(forest_reg, X_train, y_train, X_test, y_test)

    # enviando as métricas para os metadados do Airflow.
    ti.xcom_push(key='mean_abs_error', value=mean_abs_error)

def _choose_best_model(ti):
    models = [   
                 "LinearRegression"
                ,"AdaBoostRegressor"
                ,"GradientBoostingRegressor"
                ,"DecisionTreeRegressor"
                ,"RandomForestRegressor"
            ]
    
    metricas = ti.xcom_pull(
                 key='mean_abs_error'
                ,task_ids=[
                     "train_model_regression_linear"
                    ,"train_model_ada_boost_regressor"
                    ,"train_model_gradient_boosting_regression"
                    ,"train_model_decision_tree_regressor"
                    ,"train_model_random_forest_regressor"
                ]
            )
    index_best_model = metricas.index(min(metricas))
    
    print('Melhor modelo: {}, Score: {}'.format(models[index_best_model],metricas[index_best_model]))
    
    # enviando o melhor modelo para os metadados.
    ti.xcom_push(key='best_model', value=models[index_best_model])

def _final_model_train_dump(ti):
    # carregando os dados a partir da área de staging.
    X_train, y_train, X_test, y_test = load_files_train_test_from_staging()
    
    # concatenando os conjuntos de features e classes.
    X = np.concatenate((X_train, X_test), axis=0)
    y = np.concatenate((y_train, y_test), axis=0)

    # busca o melhor modelo a partir dos metadados.
    best_model = ti.xcom_pull(
                 key='best_model'
                ,task_ids=["choose_best_model"]
            )

    # verifica qual o melhor modelo.
    if best_model == "LinearRegression":
        estimator = LinearRegression()
    elif best_model == "AdaBoostRegressor":
        estimator = AdaBoostRegressor()
    elif best_model == "GradientBoostingRegressor":
        estimator = GradientBoostingRegressor()
    elif best_model == "DecisionTreeRegressor":
        estimator = DecisionTreeRegressor()
    else:
        estimator = RandomForestRegressor()

    print(estimator)

    estimator.fit(X,y)

    joblib.dump(estimator,staging_area+"/model.pkl")

with DAG('pipeline_data_science_housing_price', schedule_interval='@daily', default_args=args) as dag:
    
    load_dataset_properties_to_staging_task = PythonOperator(
        task_id = "load_dataset_properties_to_staging",
        python_callable = _load_dataset_properties_to_staging,
        email_on_failure = True,
        email = engineering_team 
    )

    load_dataset_train_to_staging_task = PythonOperator(
        task_id = "load_dataset_train_to_staging",
        python_callable = _load_dataset_train_to_staging,
        email_on_failure = True,
        email = engineering_team
    )

    join_datasets_task = PythonOperator(
        task_id = "join_datasets",
        python_callable = _join_datasets,
        email_on_failure = True,
        email = engineering_team
    )

    check_remove_duplicated_rows_task = PythonOperator(
        task_id = "check_remove_duplicated_rows",
        python_callable = _check_remove_duplicated_rows,
        email_on_failure = True,
        email = engineering_team
    )

    drop_columns_percent_missing_values_task = PythonOperator(
        task_id = "drop_columns_percent_missing_values",
        python_callable = _drop_columns_percent_missing_values,
        op_kwargs={   
               'percent_limit': 0.6
            },
        email_on_failure = True,
        email = engineering_team
    )

    transform_rescale_features_task = PythonOperator(
        task_id = "transform_rescale_features",
        python_callable = _transform_rescale_features,
        email_on_failure = True,
        email = engineering_team
    )

    fill_missing_values_task = PythonOperator(
        task_id = "fill_missing_values",
        python_callable = _fill_missing_values,
        email_on_failure = True,
        email = engineering_team
    )

    encode_categorical_valiables_task = PythonOperator(
        task_id = "encode_categorical_valiables",
        python_callable = _encode_categorical_valiables,
        email_on_failure = True,
        email = engineering_team
    )

    drop_repetitive_useless_data_task = PythonOperator(
        task_id = "drop_repetitive_useless_data",
        python_callable = _drop_repetitive_useless_data,
        email_on_failure = True,
        email = engineering_team
    )

    preprocessing_separate_train_test_task = PythonOperator(
        task_id = "preprocessing_separate_train_test",
        python_callable = _preprocessing_separate_train_test,
        email_on_failure = True,
        email = science_team

    )

    train_model_regression_linear_task = PythonOperator(
        task_id = "train_model_regression_linear",
        python_callable = _train_model_regression_linear,
        email_on_failure = True,
        email = science_team
    )

    train_model_ada_boost_regressor_task = PythonOperator(
        task_id = "train_model_ada_boost_regressor",
        python_callable = _train_model_ada_boost_regressor,
        email_on_failure = True,
        email = science_team
    )

    train_model_gradient_boosting_regression_task = PythonOperator(
        task_id = "train_model_gradient_boosting_regression",
        python_callable = _train_model_gradient_boosting_regression,
        email_on_failure = True,
        email = science_team
    )

    train_model_decision_tree_regressor_task = PythonOperator(
        task_id = "train_model_decision_tree_regressor",
        python_callable = _train_model_decision_tree_regressor,
        email_on_failure = True,
        email = science_team
    )

    train_model_random_forest_regressor_task = PythonOperator(
        task_id = "train_model_random_forest_regressor",
        python_callable = _train_model_random_forest_regressor,
        email_on_failure = True,
        email = science_team
    )
    
    choose_best_model_task = PythonOperator(
        task_id = "choose_best_model",
        python_callable = _choose_best_model,
        email_on_failure = True,
        email = science_team
    )

    final_model_train_dump_task = PythonOperator(
        task_id = "final_model_train_dump",
        python_callable = _final_model_train_dump,
        email_on_failure = True,
        email = science_team
    )

[
     load_dataset_properties_to_staging_task
    ,load_dataset_train_to_staging_task
] >> join_datasets_task >> check_remove_duplicated_rows_task >> drop_columns_percent_missing_values_task >> transform_rescale_features_task >> fill_missing_values_task >> encode_categorical_valiables_task >> drop_repetitive_useless_data_task >> preprocessing_separate_train_test_task >> [
         train_model_regression_linear_task
        ,train_model_ada_boost_regressor_task
        ,train_model_gradient_boosting_regression_task
        ,train_model_decision_tree_regressor_task
        ,train_model_random_forest_regressor_task
    ] >> choose_best_model_task >> final_model_train_dump_task
