# Text-summarisation-microservice

## Introduction

Python, FastAPI, Postgres, docker, github actions, openapi, this project has it all! The idea was to create a production ready `api` using TDD which can easily be cloned and changed to suit your needs.

I was fascinated by FastApi, and speared on with my love for Python and docker, I dived right on in to build this beauty. Alright, enough of the small talk, let's take this `baby` for a spin.

# Pre-requisites

I am assuming you, the reader have the following installed:

- [Python](https://www.python.org/) 3.9 or higher. (This app was developed using python 3.9)
- [Docker](https://docs.docker.com/engine/install/)

If not, don't panic, just click on those links and install them for your particular operating system.

### Note

When i put this app together i used `ubuntu wsl`. It should work just fine on linux/mac os environments.

# Running the app

I have used [make](https://makefiletutorial.com/) keep things simple. The app uses docker images for development and production.

1. Create a local environment: `python -m venv venv`.
2. Activate your local environment: `. venv/bin/activate` or `source venv/bin/activate`.
3. Install [httpie](https://httpie.io/): `python -m pip install httpie`.
5. Issue the `make mig` command from the cli.
6. Issue the `make up` command from the cli.

That should now be up and running, let's check if it is.

From the command line run: `http GET http://localhost:8004/ping`

You should get the follwoing output (might differ a little):

```
HTTP/1.1 200 OK
content-length: 52
content-type: application/json
date: Tue, 19 Jul 2022 10:26:37 GMT
server: uvicorn

{
    "environment": "dev",
    "ping": "pong!",
    "testing": false
}
```
The system us now up and running.

Open your browser and go to the following url: `http://localhost:8004/docs`. You should see the openapi spec.

## Test drive

Let's take it for a test drive. All these commands are issued from the command line.

i) POST

`http --json POST http://localhost:8004/summaries/ url=http://bbc.co.uk/business`

```
HTTP/1.1 201 Created
content-length: 42
content-type: application/json
date: Tue, 19 Jul 2022 10:36:26 GMT
server: uvicorn

{
    "id": 1,
    "url": "http://bbc.co.uk/business"
}
```
Wait about 30 seconds before continuing.

ii) GET 

`http --json GET http://localhost:8004/summaries/1/`

```
HTTP/1.1 200 OK
content-length: 1044
content-type: application/json
date: Tue, 19 Jul 2022 10:40:30 GMT
server: uvicorn

{
    "created_at": "2022-07-19T10:36:26.416954+00:00",
    "id": 1,
    "summary": " You should see a summary here"
}

```

iii) PUT

`http --json PUT http://localhost:8004/summaries/1/ url=http://bbc.co.uk/business summary="ipsum lorem"`

```
HTTP/1.1 200 OK
content-length: 114
content-type: application/json
date: Tue, 19 Jul 2022 10:50:30 GMT
server: uvicorn

{
    "created_at": "2022-07-19T10:49:10.074827+00:00",
    "id": 1,
    "summary": "ipsum lorem",
    "url": "http://bbc.co.uk/business"
}
```

iv) GET (all summaries)

`http GET http://localhost:8004/summaries/`

```
HTTP/1.1 200 OK
content-length: 116
content-type: application/json
date: Tue, 19 Jul 2022 10:53:00 GMT
server: uvicorn

[
    {
        "created_at": "2022-07-19T10:49:10.074827+00:00",
        "id": 1,
        "summary": "ipsum lorem",
        "url": "http://bbc.co.uk/business"
    }
]
```

v) DELETE

`http --json DELETE http://localhost:8004/summaries/1/`

```
HTTP/1.1 200 OK
content-length: 42
content-type: application/json
date: Tue, 19 Jul 2022 10:54:36 GMT
server: uvicorn

{
    "id": 1,
    "url": "http://bbc.co.uk/business"
}
```

Please feel free to add more URL's. You can also interact with the api via the web page `http://localhost:8004/docs`.

When you have had enough fun playing with the service, type `make down` into the cli and the service will terminate.

## github actions

Take a look in the `/github/workflows/build_docker_image.yml` There you have an example of how you can push to a docker repository. For pushing to cloud environments you would need to scope in your cloud environment credentials into the workflow.

## Testing

I prefer to write tests before the code. I have shown both examples of `unit` and `end to end` testing. To run the tests, from the cli, run `make tests`. Run `make testcov` to see a coverage report. You can also run the test quicker in parallel `make test_parallel`

