// FROM python:3.8-alpine

// COPY ./requirements.txt /app/requirements.txt

// WORKDIR /app

// RUN pip3 install -r requirements.txt 

// COPY . /app

// ENTRYPOINT ["python"]

// CMD ["flask_test.py"]

FROM ubuntu:20.04
RUN apt-get -y update
RUN apt-get -y install nginx