FROM apache/airflow:latest

#use the user airflow
USER airflow

RUN pip install apache-airflow-providers-docker \
&&  pip install apache-airflow-providers-http \
&&  pip install apache-airflow-providers-airbyte \

#Go ack to user root
USER root

