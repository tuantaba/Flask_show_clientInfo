FROM python:2.7
#https://hub.docker.com/_/python

COPY ./data /opt/showclient_app

WORKDIR /opt/showclient_app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
