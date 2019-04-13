FROM golang:alpine

RUN apk add --no-cache git \
    && go get -u github.com/labstack/echo/...

WORKDIR /app

ADD . /app
