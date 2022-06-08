FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /mystore
WORKDIR /mystore
ADD requirements.txt /mystore/
RUN pip install -r requirements.txt
ADD . /mystore/