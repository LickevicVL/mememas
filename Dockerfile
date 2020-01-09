FROM python:3.8-alpine

ARG PROJECT_DIR

RUN apk update --no-cache \
    && apk add --no-cache gcc \
    && apk add --no-cache postgresql-libs \
    && apk add --no-cache postgresql-dev \
    && apk add --no-cache zlib-dev \
    && apk add --no-cache jpeg-dev \
    && apk add --no-cache musl-dev \
    && apk add --no-cache libmagic \
    && pip install pip -U

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PROJECT_DIR ${PROJECT_DIR:-/var/app/mememas}

WORKDIR $PROJECT_DIR
COPY . .


CMD sh runserver.sh
