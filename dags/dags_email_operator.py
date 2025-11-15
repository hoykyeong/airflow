import pendulum
import datetime

from airflow.providers.smtp.operators.smtp import EmailOperator
from airflow.sdk import DAG

with DAG(
    dag_id = "dags_bash_select_fruit",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    send_email_task = EmailOperator(
        task_id = "send_email_task",
        conn_id = 'conn_smtp_gmail',
        to='hyoee@pusan.ac.kr',
        subject="airflow 성공 메일",
        html_content="airflow 작업이 완료되었습니다."
    )