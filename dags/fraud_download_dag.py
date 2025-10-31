from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta
import subprocess



def download_data():
    script_path = '/usr/local/airflow/scripts/download_kaggle_data.py'
    subprocess.run(['python', script_path], check=True)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'reties':1,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='fraud_download_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['fraud','etl','kaggle']
) as dag: 
    download_task = PythonOperator(
        task_id='download_fraud_data',
        python_callable=download_data
    )

    download_task