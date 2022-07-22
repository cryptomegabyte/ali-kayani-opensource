dev_requirements:
	python -m pip install pre-commit

precommit:
	pre-commit run --all-files

run_containers:
	docker run --name taxi-postgres -p 5432:5432 \
    -e POSTGRES_USER=taxi -e POSTGRES_DB=taxi -e POSTGRES_PASSWORD=taxi -d postgres
	docker run --name taxi-redis -p 6379:6379 -d redis
	docker exec -it some-redis redis-cli ping

mig:
	python server/manage.py migrate

create_superuser:
	python server/manage.py createsuperuser

runserver:
	python server/manage.py runserver

stop_containers:
	docker stop taxi-postgres
	docker stop taxi-redis

clean_containers:
	docker system prune -af
