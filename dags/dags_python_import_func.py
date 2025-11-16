import pendulum
import datetime

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG

# from plugins.common.common_func import get_sftp
# airflow는 plugins까지 잡혀있어서 에러가 남
from common.common_func import get_sftp

with DAG(
    dag_id = 'dags_python_import_func',
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025,11,14, tz="Asia/Seoul"),
    catchup=False
) as dag:
    task_get_sftp = PythonOperator(
        task_id = 'task_get_sftp',
        python_callable=get_sftp
    )