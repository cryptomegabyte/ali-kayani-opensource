# Brings the app up
up: docker-compose.yml	requirements-dev.txt docker/Dockerfile.dev	db/Dockerfile.db
	docker-compose up -d --build

# Stops the app
down:  docker-compose.yml
	docker-compose down -v

# Runs the db migrations
mig:
	docker-compose exec web aerich upgrade

# Logs into the web container
login_web:
	docker-compose exec web bash

# Logs into the postgres db
login_db:
	docker-compose exec web-db psql -U postgres

# Allows the user to log into postgres when container is running
postgres:
	docker-compose exec web-db psql -U postgres

# Runs the tests when the containers are running
test:
	docker-compose exec web python -m pytest -rP -v

# displays the test coverage
testcov:
	docker-compose exec web python -m pytest --cov="."

# run tests in parallel
test_parallel:
	docker-compose exec web pytest -rP -k "unit" -n auto

# runs pre-commit
precommit:
	pre-commit run --all-files

# runs production docker file locally
start_local_prod:
	docker build -f docker/Dockerfile.prod -t web .
	docker run -d --name tsm-prod -e PORT=8765 -e DATABASE_URL=sqlite://sqlite.db -p 5003:8765 web:latest

# stops production docker file from running locally
stop_local_prod:
	docker rm tsm-prod -f
