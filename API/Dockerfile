FROM python:2.7

MAINTAINER gurumurthy

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "Master.py" ]