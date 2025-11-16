import pendulum
import datetime
import random

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG

with DAG(
    dag_id="dags_python_operator", # 파이썬 파일명과 상관 없음, 일반적으로 파일명과 dags 일치시키는 것이 좋음
    schedule="6 30 * * *", # 분, 시, 일, 월, 요일 -> 매일 0시 0분마다 돈다
    start_date=pendulum.datetime(2025, 11, 14, tz="Asia/Seoul"), # dag이 언제부터 돌것인지
    catchup=False, # 돌린시점과 시작 시점 사이에 누락된 구간을 돌리지 않음, 일반적으로 False
    # dagrun_timeout= datetime.timedelta(minutes=60), # 60분 이상 돌면 실패
    # tags=["example", "example2", "example3"],
) as dag:
    # 파이썬 오퍼레이터는 파이썬 함수를 실행시켜줌
    # 우선 함수 정의
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        # 랜덤 값 추출
        rand_int = random.randint(0,3) # 0~3 까지의 값 추출
        print(fruit[rand_int]) # 리스트 중 하나의 과일을 선택하여 출력
    
    # task 생성
    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable=select_fruit
    )

    py_t1