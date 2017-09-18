FROM python:2.7

MAINTAINER gurumurthy

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY minions/minionServers.py /app/minions
COPY minions/__init__.py /app/minions

COPY src/__init__.py /app/src
COPY src/Master.py /app/src


RUN ls -la /app/src/*
RUN ls -la /app/minions/*

ENTRYPOINT [ "python" ]
CMD [ "/app/src/Master.py" ]