from datetime import datetime
from airflow import DAG
from docker.types import Mount
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.docker.operators.docker import DockerOperator
import subprocess

CONN_ID= ''

default_args ={
    'owner': 'airflow' ,# type: ignore
    'depends_on_past' : False,
    'email_on_failure' : False,
    'email_on_retry' : False,
}


dag=DAG(
    'elt_and_dbt',
    default_args=default_args,
    description="this DAG containes 2 tasks for running elt script and dt container",
    start_date=datetime(2024, 2, 24),
    catchup=False
)

t1=AirbyteTriggerSyncOperator(
    task_id="airbyte_postgres_postgres",
    airbyte_conn_id='airbyte',
    connection_id= CONN_ID ,
    asynchronous=False,
    timeout=3600,
    wait_seconds=3,
    dag=dag
)

t2 = DockerOperator(
    task_id="run_dbt",
    image= 'ghcr.io/dbt-labs/dbt-postgres:1.4.7',
    command=[
        "run",
        "--profiles-dir",
        "/root",
        "--project-dir",
        "/dbt"
    ],
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge" ,
    mounts=[
        Mount(source='F:/elt/custom_postgres',
              target='/dbt', type='bind'),
        Mount(source='C:/Users/Prasad/.dbt',
              target= '/root',type='bind')

        
    ],
    dag=dag
)
             
t1 >> t2           
             


             
             
             









