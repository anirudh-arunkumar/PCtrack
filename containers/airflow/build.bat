rmdir /s dags
mkdir dags
xcopy ..\..\py\airflow\dags\* dags\ /e

docker build -t itracker_airflow .