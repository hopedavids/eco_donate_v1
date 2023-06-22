# Download an official python runtime as the base image
FROM python:3.11-slim

#create the working directory in container
RUN mkdir /app

#add labels to the application
LABEL maintainer="Hope Davids <hledavids@gmail.com>,\
                Emmanuel Davids <emmanueldavids417@gmail.com>,\
                Bernard Sakyi <sakyibernard77@gmail.com>"

LABEL version="1.0"
LABEL description="Eco_Donate Project"
LABEL tag="eco_donate_v1.0"

# set the environment variable of buffer to True or 1
ENV PYTHONUNBUFFERED 1

#copied the requirements file to the container
COPY ./requirements.txt /requirements.txt

# install all the requirements using pip
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

#set the current working directory
WORKDIR /app

#Copy all the resources and file in donate to the app directory
COPY ./donate /app

# create user dev
RUN useradd -ms /bin/bash dev

# activate and the dev user
USER dev

CMD ["flask","run","--host=0.0.0.0"]
