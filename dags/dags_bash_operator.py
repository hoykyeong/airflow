import pendulum
import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_operator", # 파이썬 파일명과 상관 없음, 일반적으로 파일명과 dags 일치시키는 것이 좋음
    schedule="0 0 * * *", # 분, 시, 일, 월, 요일 -> 매일 0시 0분마다 돈다
    start_date=pendulum.datetime(2025, 11, 14, tz="Asial/Seoul"), # dag이 언제부터 돌것인지
    catchup=False, # 돌린시점과 시작 시점 사이에 누락된 구간을 돌리지 않음, 일반적으로 False
    # dagrun_timeout= datetime.timedelta(minutes=60), # 60분 이상 돌면 실패
    # tags=["example", "example2", "example3"],
) as dag:
    bash_t1 = BashOperator(
        task_id = "bash_t1",
        bash_command= "echo whoami" # 어떤 쉘스크립트를 쓸 것인지
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command= "echo $HOSTNAME"  # DESKTOP-19JBBGV
    )

    bash_t1 >> bash_t2