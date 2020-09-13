FROM ubuntu:latest
MAINTAINER lavacano@lavacano.net
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
RUN rm /app/requirements.txt

COPY app/ /app/

EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["init.py"]
