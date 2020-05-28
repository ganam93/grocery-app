FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /grocery
WORKDIR /grocery
COPY ./grocery /grocery

RUN adduser -D user
USER user


