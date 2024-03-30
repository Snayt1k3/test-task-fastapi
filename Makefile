black:
	poetry run black .

app:
	poetry run python main.py

db:
	alembic upgrade head

start: db app
