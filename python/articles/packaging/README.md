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

```python
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

```python
def add(x:int, y:int) -> int:
    return x + y
```

## add_app/__init__.py

```python
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

```python
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

## Installing locally

Ensure you are within the `packaging/apps` folder. `pip install .` will install the package locally. If you want to make the package available to other users of the system then `pip install -e .` will make that happen.

## Using the package

Open your pthon repl by typing `python` at the command prompt, import the app then call the add function.

```python
Python 3.10.5 (main, Aug  2 2022, 15:16:15) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import add_app
>>> print(add_app.add(5,3))
8
>>> 
```

Success! the app has been imported and used successfully.

## Dependencies

Using other packages is quite normal when developing python pacakges. The package we are devloping can depend on another package, we want to make sure the consumer of our package is able to use our package correctly without having to manually download those dependencies.

Here is how that can be done, I am just inventing a name of a package called `silicon`.

```python

import silicon

def add(x:int, y:int) -> int:
    silicon.tell_a_joke()
    return x + y

```

The add function now depends on the silicon package. `setup.py` needs to be modified so when our package is installed it will automatically install the `silicon` package.

```python
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
      install_requires=[
          'silicon',
      ],
      zip_safe=False
)
```

`install_requires` is a list of packages. Once done issuing the command `python setup.py develop` will show you the packages that are being installed. Please note that adding packages like this assumes that the external package has been published on `pypi`.

`setup.py` can also be modified to download packages from other sources. Here is how you would do that.

```python
setup(
    ...
    dependency_links=['https://repository/repo/tarball/master#egg=package-1.0']
    ...
)
```

## Publishing

We have an amazing app, it needs to be published so it can be consumed by our users. There are private and public respositories that enable you to store your code. [Pypi](https://pypi.org/) is a public repository of packages where you can store python packages.

In my professional experience, I usually will use a CI/CD tool such as github actions to build and deploy my package to a specific location.

`python setup.py sdist` will create a `dist/` which contains a tar file, this tar file can then be uploaded to a package repository.

