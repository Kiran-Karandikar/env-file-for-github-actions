FROM python:3.9-alpine3.13
LABEL maintainer="khkarandikar@gmail.com"

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

COPY ./base /base
COPY ./base/requirements /tmp/requirements
WORKDIR /base

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache  \
      build-base bash make alpine-sdk musl-dev && \
    /py/bin/pip install -r /tmp/requirements/local.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        app-user

ENV PATH="/py/bin:$PATH"

USER app-user
