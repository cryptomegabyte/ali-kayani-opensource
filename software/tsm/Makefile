up: docker-compose.yml	requirements.txt Dockerfile	db/Dockerfile
	docker-compose up -d --build

down:  docker-compose.yml
	docker-compose down -v

test:
	docker-compose exec web python3 -m pytest

clean:
	rm -rf venv env
