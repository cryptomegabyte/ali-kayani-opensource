.PHONY: all

requirements:
	python -m pip install -r requirements.txt

precommit:
	pre-commit run --all-files

run_containers:
	docker run --name taxi-postgres -p 5432:5432 \
    -e POSTGRES_USER=taxi -e POSTGRES_DB=taxi -e POSTGRES_PASSWORD=taxi -d postgres
	docker run --name taxi-redis -p 6379:6379 -d redis
	docker exec -it taxi-redis redis-cli ping

set_exports:
	./exports.sh

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

tests:
	python server/manage.py test -v 2 trips.tests
	python -m pytest server/trips/tests/test_websocket.py -v -rP
