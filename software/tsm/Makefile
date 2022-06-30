# Brings the app up
up: docker-compose.yml	requirements.txt docker/Dockerfile.dev	db/Dockerfile
	docker-compose up -d --build

# Stops the app
down:  docker-compose.yml
	docker-compose down -v

# Runs the tests when the containers are running
test:
	docker-compose exec web python3 -m pytest -rP

postgres:
	docker-compose exec web-db psql -U postgres

mig:
	docker-compose exec web aerich upgrade

test:
	docker-compose exec web python -m pytest -rP -v

testcov:
	docker-compose exec web python -m pytest --cov="."

	