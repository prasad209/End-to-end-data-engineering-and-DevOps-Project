
https://github.com/prasad209/End-to-end-data-engineering-and-DevOps-Project/assets/79194792/8bf23ea0-57d0-46f3-82bc-4fd8c0cfa317

Aim:This is an ongoing Data engineering+ DevOps projects
Data from source database is extracted and loaded to a destination database using a python ELT script, the data received
in this destination database is transfotmed using dbt
In total, there are 4 docker containers

Docker 1: consists of source postgresql database

Docker 2:python ELT script 

Docker 3:consists of destination postgresql database

Docker 4: dbt

The project uses
tech stack: Docker container, python, dbt 
Database: pgsql

Folder structure:
Custom_postgres : folder contains dbt files like project.yaml, containes SQL scripts, schema. sql where you can find the description and tests on each column

etl: this folder contains a python script for etl which extracts data from source postgres container and dumps it in a file and then loads data from this file to destination postgresql 
the script checks connection to databases also. 

docker_compose.yaml:the yaml file states the container services required as stated at the start of this readme doc. it also states the docker network📡 for this project and it's type. 
