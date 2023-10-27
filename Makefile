.PHONY: install
install:
	poetry install

.PHONY: run-server
run-server:
	poetry run python manage.py runserver	

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

.PHONY: shell
shell:
	poetry run python manage.py shell

.PHONY: update
update: install migrate ;