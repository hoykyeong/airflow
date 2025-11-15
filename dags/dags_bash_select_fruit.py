import pendulum
import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

with DAG(
    dag_id = "dags_bash_select_fruit",
    schedule="10 0 * * 6#1", # 첫번째 주 토요일(6) 0시 10분
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    t1_orange = BashOperator(
        task_id = "t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE" # task를 실행하는 주체는 worker 컨테이너이고, 위치를 알기 위해 이렇게 경로를 설정함
    )

    t2_avocado = BashOperator(
        task_id = "t2_avocado",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO"
    )

    t1_orange >> t2_avocado