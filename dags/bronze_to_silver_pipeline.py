from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "data-engineering",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="aws_data_lakehouse_pipeline",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
) as dag:

    ingest_data = BashOperator(
        task_id="api_ingestion",
        bash_command="python /opt/airflow/ingestion/api_ingestion.py"
    )

    spark_job = BashOperator(
        task_id="spark_transformation",
        bash_command="""
        spark-submit 
        /opt/airflow/spark_jobs/silver_transformation.py
        """
    )

    ingest_data >> spark_job