.PHONY: all

up:
	docker-compose up -d --build
	make mig

mig:
	docker-compose exec taxi-server python manage.py migrate

create_superuser:
	docker-compose exec taxi-server python manage.py createsuperuser

unit_tests:
	docker-compose exec taxi-server python -m pytest
	cd client && yarn test

integration_tests:
	cd client && yarn integration_tests
	
down:  docker-compose.yml
	docker-compose down -v

clean:
	docker system prune -af

precommit:
	pre-commit run --all-files
