FROM python:3.12

WORKDIR /code

EXPOSE 8000

COPY . .

RUN pip install poetry
RUN poetry install
