FROM python:3.7-alpine

MAINTAINER Arshad Hosein <iarsh930@gmail.com>

ENV INSTALL_PATH /moe

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .