import pendulum
from airflow.sdk import dag, task


# dag_id는 반드시 유니크하게 설정하세요.
@dag(
    dag_id='hyokyung_taskflow_test_v1',   # ✔ 충돌 방지용 고유 이름
    schedule='0 2 * * 1',                 # 매주 월요일 02:00
    start_date=pendulum.datetime(2025, 11, 14, tz='Asia/Seoul'),
    catchup=False
)
def hyokyung_taskflow_test():

    # TaskFlow 기반 Task
    @task(task_id="print_context")
    def print_context(some_input: str):
        print(some_input)
        return "task finished"

    # Task 생성 (호출 = 실행 X / Task 객체 생성)
    print_context("taskflow decorator 테스트 중입니다.")


# DAG 인스턴스 생성 (이 줄 없으면 DAG 등록 안 됨)
example = hyokyung_taskflow_test()


# from airflow.decorators import task

# with DAG(
#     dag_id = 'dags_python_task_decorator',
#     schedule='0 2 * * 1',
#     start_date=pendulum.datetime(2025, 11, 14, tz='Asia/Seoul'),
#     catchup=False
# ) as dag:
    
#     @task(task_id = 'python_task_1')
#     def print_context(some_input):
#         print(some_input)
#     python_task_1 = print_context('task_decorator 설명')





# @task
# def print_context(some_input):
#     print(some_input)
# with DAG(dag_id = 'dags_python_task_decorator',
#          schedule='0 2 * * 1',
#          start_date=pendulum.datetime(2025, 11, 14, tz='Asia/Seoul'),
#          catchup=False):
#     python_task_1 = print_context("task_decorator 실행")