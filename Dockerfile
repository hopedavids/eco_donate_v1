FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app

COPY ./donate /app

RUN useradd -ms /bin/bash dev

USER dev

