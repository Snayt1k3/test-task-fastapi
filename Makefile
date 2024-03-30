black:
	poetry run black .

app:
	poetry run uvicorn main:app --host 0.0.0.0 --proxy-headers

db:
	poetry run alembic upgrade head

start: db app

script:
	poetry run python script.py