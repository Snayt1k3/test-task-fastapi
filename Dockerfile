FROM python:3.12

WORKDIR /code

COPY . .

RUN pip install poetry
RUN poetry install
