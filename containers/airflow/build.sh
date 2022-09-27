rm -Rf dags/*
cp -R ../../py/airflow/dags/* dags/
docker build -t itracker_airflow .
