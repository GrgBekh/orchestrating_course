FROM apache/airflow:2.7.1


WORKDIR /opt/airflow


USER root

RUN apt-get update -y\
    && apt-get install -y python3 python3-dev gcc gfortran musl-dev \
    && apt-get install -y procps default-jre
    

USER airflow

RUN pip install numpy

COPY ./dags ./dags
COPY --chown=airflow . .

EXPOSE 8080
