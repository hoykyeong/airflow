from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = 'dags_bash_with_template',
    start_date=pendulum.datetime(2025,11,14, tz='Asia/Seoul'),
    schedule='10 0 * * *',
    catchup=False
) as dag:
    bash_t1 = BashOperator(
        task_id = 'bash_t1',
        bash_command='echo "data_interval_end: {{data_interval_end}}"'
    )
    bash_t2 = BashOperator(
        task_id = 'bash_t2',
        env =  {
            'START_DATE' : '{{data_interval_start | ds}}', # dash가 붙어있는 10자리 형식을 위해 ds 추가
            'END_DATE' : '{{data_interval_end | ds}}' # airflow 3.0에서 data_interval_start값과 data_interval_end값이 동일하게 출력됨
        },
        bash_command='echo $START_DATE && echo $END_DATE' 
        # START_DATE 출력, 만약 해당 출력이 성공하면(&&) END_DATE 출력
    )

    bash_t1 >> bash_t2