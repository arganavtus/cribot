FROM python:3.12-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential libssl-dev libffi-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
ENV POETRY_VERSION=1.7.1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /usr/src/app/cribot

COPY pyproject.toml poetry.lock /usr/src/app/cribot

RUN poetry config virtualenvs.create false && poetry install --no-root --only main

COPY . /usr/src/app/cribot
