from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id='dags_bash_with_macro_eg1',
    schedule='10 0 L * *', # 매월 말일에 수행, 0시 10분에 수행
    start_date=pendulum.datetime(2025, 11, 14, tz='Asia/Seoul'),
    catchup=False
) as dag:
    bash_task_1 = BashOperator(
        task_id = 'bash_task_1',
        # START_DATE : 전월 말일, END_DATE : 1일전(배치 돌기)
        env = {'START_DATE' : '{{data_interval_start.in_timezone("Asia/Seoul") | ds}}',
                'END_DATE' : '{{(data_interval_end.in_timezone("Asia/Seoul") - macros.deteutil.relativedelta.relativedleta(days=1))| ds}}'},
        bash_command = 'echo "START_DATE : $START_DATE" && echo "END_DATE : $END_DATE"'
    )