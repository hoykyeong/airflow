import pendulum
from airflow.sdk import DAG, task

with DAG(
    dag_id = 'dags_python_task_decorator',
    schedule='0 2 * * 1', # 매주 월요일 2시 0분에 도는 스케줄
    # @once, @daliy, @weelky, @month;y, @yearly
    start_date=pendulum.datetime(2025, 11, 14, tz='Asia/Seoul'),
    catchup=False
) as dag:
    @task(task_id="python_task_1") # task 데커레이터, 인자는 파이썬 오퍼레이터에서의 주도한 task_id랑 같은 파라미터
    def print_context(some_input):
        print(some_input)

    python_task_1 = print_context("task_decorator 실행")