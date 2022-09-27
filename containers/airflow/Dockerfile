FROM apache/airflow:2.0.0

ARG AIRFLOW_USER_HOME=/usr/local/airflow
ARG AIRFLOW_HOME=/opt/airflow

COPY scripts/entrypoint.sh /entrypoint.sh
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
COPY dags/* ${AIRFLOW_HOME}/dags/

EXPOSE 8080 5555 8793

WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]