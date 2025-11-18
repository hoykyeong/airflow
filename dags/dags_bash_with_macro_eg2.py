from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id='dags_bash_with_macro_eg2',
    schedule='10 0 * * 6#2', #매월 둘째주 토요일
    start_date=pendulum.datetime(2025, 11, 14, tz='Asia/Seoul'),
    catchup=False
) as dag:
    bash_task_2 = BashOperator(
        task_id = 'bash_task_2',
        # START_DATE : 2주전 월요일, END_DATE : 2주전 토요일
        env = {'START_DATE' : '{{(data_interval_end.in_timezone("Asia/Seoul") - macros.deteutil.relativedelta.relativedleta(days=19))| ds}}',
        'END_DATE' : '{{(data_interval_end.in_timezone("Asia/Seoul") - macros.deteutil.relativedelta.relativedleta(days=14))| ds}}'},
        bash_command = 'echo "START_DATE : $START_DATE" && echo "END_DATE : $END_DATE"'
    )