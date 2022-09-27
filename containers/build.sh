docker volume create itrackerdb
docker volume create itrackertemp
docker volume create itracker_pgdb

docker build -t itrackerwebadmin ../web/itracker_web_admin

cd airflow
./build.sh
