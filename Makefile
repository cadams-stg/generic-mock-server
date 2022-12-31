build:
	docker compose build

run:
	docker-compose up

destroy:
	docker-compose down -v

rebuild: destroy build run

makemigrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate

bash:
	docker-compose run web bash

data:
	docker compose run web python manage.py seed_data

shell:
	docker-compose run web python manage.py shell_plus

lint:
	isort .
	black .

test:
	docker-compose run web /code/test/check_all_endpoints.sh
