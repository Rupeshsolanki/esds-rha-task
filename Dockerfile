
FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8


RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN   pip3 install -r requirements.txt
 
ENV FLASK_APP=apprha.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0","--port=8080"]

