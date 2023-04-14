FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt install -y build-essential libpq-dev

RUN apt-get -y install curl
RUN apt-get -y install python3.10

WORKDIR /src

COPY . .

RUN curl -sSL https://install.python-poetry.org | python3.10 -

ENV PATH="${PATH}:/root/.local/bin"

RUN poetry install
RUN poetry run pip install psycopg2-binary --no-binary psycopg2-binary
