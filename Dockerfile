FROM python:3.9-slim

MAINTAINER lukas.kucera.g@protonmail.com

# python-magic linux only depenency
RUN apt-get update && apt-get install -y libmagic1

RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE $PORT
CMD ['scripts/run.sh']
