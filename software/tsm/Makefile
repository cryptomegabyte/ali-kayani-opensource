# Brings the app up
up: docker-compose.yml	requirements.txt docker/Dockerfile.dev	db/Dockerfile.db
	docker-compose up -d --build

# Stops the app
down:  docker-compose.yml
	docker-compose down -v

# Runs the db migrations
mig:
	docker-compose exec web aerich upgrade

# Allows the user to log into postgres when container is running
postgres:
	docker-compose exec web-db psql -U postgres

# Runs the tests when the containers are running
test:
	docker-compose exec web python -m pytest -rP -v

# displays the test coverage
testcov:
	docker-compose exec web python -m pytest --cov="."

# runs pre-commit
precommit:
	pre-commit run --all-files
