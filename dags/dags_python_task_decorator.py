import pendulum
from airflow.sdk import dag, task

@dag(
    schedule='0 2 * * *',
    start_date=pendulum.datetime(2025, 1, 1, tz='Asia/Seoul'),
    catchup=False
)
def dags_python_task_decorator():

    @task(task_id="print_the_context")
    def print_context(some_input):
        print(some_input)
        return "Whatever you return gets printed in the logs"

    print_context('task_decorator 설명')

example_dag = dags_python_task_decorator()