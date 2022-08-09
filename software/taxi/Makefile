.PHONY: all

up_local:
	docker-compose up -d --build

mig:
	docker-compose exec taxi-server python manage.py migrate

create_superuser:
	docker-compose exec taxi-server python manage.py createsuperuser

tests:
	docker-compose exec taxi-server python -m pytest
	docker-compose exec taxi-server python -m test -v 2 trips.tests
	

down_local:  docker-compose.yml
	docker-compose down -v

clean:
	docker system prune -af

precommit:
	pre-commit run --all-files

