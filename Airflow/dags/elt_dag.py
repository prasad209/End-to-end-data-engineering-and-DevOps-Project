from datetime import datetime
from airflow import DAG
from docker.types import Mount
from airflow.operators.python_operators import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.docker import DcokerOperator
import subprocess

default_args ={
    'owner': 'airflow' # type: ignore
    'depends_on_past' : False,
    'email_on_failure' : False,
    'email_on_retry' : False,
}

def run_elt_script():
    script_path= "/opt/airflow/elt/elt_script"
    result= subprocess.run(["python",script_path],capture_output=True,text=True)
    if result.returncode =0:
        raise Exception(f"script failed with error: {result.stderr}")
    else:
        print(result.stdout)

