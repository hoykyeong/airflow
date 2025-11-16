import pendulum
from airflow.sdk import dag, task


import pendulum
from airflow.sdk import dag, task

@dag(
    dag_id='dags_python_task_decorator',
    schedule='0 2 * * 1',
    start_date=pendulum.datetime(2025, 11, 14, tz='Asia/Seoul'),
    catchup=False
)
def dags_python_task_decorator():

    @task
    def print_context(some_input):
        print(some_input)

    print_context("task_decorator 실행")

example = dags_python_task_decorator()

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