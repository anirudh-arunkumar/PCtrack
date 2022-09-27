docker volume create itrackerdb
docker volume create itrackertemp
docker volume create itracker_pgdb

:: docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")

docker build -t itrackerwebadmin ../web/itracker_web_admin