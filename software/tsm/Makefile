# Brings the app up
up: docker-compose.yml	requirements.txt Dockerfile	db/Dockerfile
	docker-compose up -d --build

# Stops the app
down:  docker-compose.yml
	docker-compose down -v

# Runs the tests when the containers are running
test:
	docker-compose exec web python3 -m pytest -rP

postgres:
	docker-compose exec web-db psql -U postgres