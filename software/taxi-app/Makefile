dev_requirements:
	python -m pip install pre-commit

precommit:
	pre-commit run --all-files

runcontainers:
	docker run --name some-postgres -p 5432:5432 \
    -e POSTGRES_USER=taxi -e POSTGRES_DB=taxi -e POSTGRES_PASSWORD=taxi -d postgres
	docker run --name some-redis -p 6379:6379 -d redis
	docker exec -it some-redis redis-cli ping

mig:
	python server/manage.py migrate

create_superuser:
	python server/manage.py createsuperuser

runserver:
	python server/manage.py runserver

cleancontainers:
	docker system prune -af