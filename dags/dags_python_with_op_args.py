from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.python import PythonOperator

from common.common_func import regist

with DAG(
    dag_id = 'dags_python_with_op_args',
    start_date=pendulum.datetime(2025,11,14, tz='Asia/Seoul'),
    schedule='30 6 * * *',
    catchup=False
) as dag:
    regist_t1 = PythonOperator(
        task_id = 'regist_t1',
        python_callable=regist,
        op_args=['hyoee','woman', 'kr', 'seoul']
    )

    regist_t1