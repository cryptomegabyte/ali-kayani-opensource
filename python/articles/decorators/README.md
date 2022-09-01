# Python Decorators

I first encountered decroators when I was loooking for a simple way to add open telemetry to a python project. I was familiar with the theory but I actually never had to use them in practice.

The project itself was rather large, altering every function would involve a lot of work, I needed a simple solution to drop into the project which wouldn't fail tests as well as adding the new telemetry logic, decorators to the rescue.

## What are decorators?

In short they are higher order functions. It's a function that takes in another function and extends it's behaviour without modifying it.

# Example

I will demonstrate the concept of a decorator through an example.  Create a folder called app.

## requirements.txt

Create a requirments.txt file in the `app/` folder and add the following text:

```
pytest
```

## venv

Create a virtual environment: `python -m venv venv`.

Activate the virtual environment: `. venv/bin/activate`

## install dependencies

Install the items packages listed within the requirements file: `python -m pip install -r requirements.txt`

## structure

Create the following folder structure within the `app/` folder.

```
app/
|---src/
|-----__init__.py
|-----multiply.py
|---tests/
|-----__init__.py
|-----test_multiply.py
```

## test_multiply.py

