# Packaging

Installing python packages with pip is simple enough, `python -m pip install <package_name>` and the package is installed for you. As a seasoned software engineer who works with python I wanted to dive a little deeper into the world of packaging, this article is an attempt to uncover how python projects can be packaged for distribution.

# Setup

Let's getting the ball ralling by getting a virtual environment setup and the requirements installed. Ensure you are within the [packaging](../packaging/) folder.

1. Create a virtual environment: `python -m venv venv`.
2. Activate the  virtual environment: `. venv/bin/activate` or `source venv/bin/activate`.
3. Install the app requirements: `python -m pip install -r requirements.txt`.

# App

I will be using a small calculator project to demonstrate the concept of packaging an app. Let's get started by creating a project structure. Within the `apps/` folder create the following project structure:

```
packaging/
|--apps/
|----add_app/
|--------src/
|----------__init__.py
|----------add.py
|--------tests/
|----------test_add.py
|--------__init__.py
|----setup.py
|--.gitignore
|--README.md
|--requirements.txt
```

Add the code below to the files shown.
## test_add.py

```
import pytest
from src.add import add

@pytest.mark.parametrize("x,y,result",[(1,2,3), (4,5,9), (6,7,13)])
def test_add(x:int, y:int, result:int) -> None:

    # given
    test_wrapper = None
    # when
    test_wrapper = add(x,y)
    # then
    assert test_wrapper == result
```

## add.py

```
def add(x:int, y:int) -> int:
    return x + y
```

## add_app/__init__.py

```
from .src.add import add
```

Ensure all those newly created file are saved and run `pytest -v -rP` and you should see the test passing.


# Packaging our app

## [Setuptools](https://setuptools.pypa.io/en/latest/index.html)

```
Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects.

It helps developers to easily share reusable code (in the form of a library) and programs (e.g., CLI/GUI tools implemented in Python), that can be installed with pip and uploaded to PyPI.
```

We will be using this tool to package our project. Please visit there website to learn more.

## setup.py

Let's get started packaging our app. We're going to create a setup.py within the `apps/` folder then we will add data to it.

1. `touch setup.py`
2. Add the following data.

```
from setuptools import setup

setup(
      name='add_app',
      version='0.1',
      description='An app that adds!',
      url='https://fakeurl.com',
      author='Foo Bar',
      author_email='foo.bar@foo.com',
      license='MIT',
      packages=['add_app'],
      zip_safe=False
)
```

This is metadata which encapsulates the package you are creating.  Go to [setuptools](https://github.com/pypa/setuptools) to learn more about the different meta data items you can potentially add.

At this point 

## Installing locally

