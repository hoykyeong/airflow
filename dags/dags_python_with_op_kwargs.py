from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.python import PythonOperator

from common.common_func import regist2

with DAG(
    dag_id = 'dags_python_with_op_kwargs',
    start_date=pendulum.datetime(2025,11,14, tz='Asia/Seoul'),
    schedule='30 6 * * *',
    catchup=False
) as dag:
    regist2_t1 = PythonOperator(
        task_id = 'regist2_t1',
        python_callable=regist2,
        op_args=['hyoee','woman', 'kr', 'seoul'],
        op_kwargs = {'email' : 'jhk2929616@gmail.com', 'phone' : '01055382768'}
    )

    regist2_t1