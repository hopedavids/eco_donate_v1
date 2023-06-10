FROM python:3.11-slim

RUN mkdir /app

LABEL maintainer="Hope Davids <hledavids@gmail.com>,\
                Emmanuel Davids <emmanueldavids417@gmail.com>,\
                Bernard Sakyi <sakyibernard77@gmail.com>"

LABEL version="1.0"
LABEL description="Eco_Donate Project"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt


WORKDIR /app

COPY ./donate /app

RUN useradd -ms /bin/bash dev

USER dev

