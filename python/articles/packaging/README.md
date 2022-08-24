# Packaging

Installing python packages with pip is simple enough, `python -m pip install <package_name>` and the package is installed for you. As a seasoned software engineer who works with python I wanted to dive a little deeper into the world of packaging, this article is an attempt to uncover how python projects can be packaged for distribution.

# Sample Project

I will be using a small calculator project to demonstrate the concept of packaging an app. This isn't the only way that you can package a python app, I will be discussing how you can package an app with `poetry` to, but first, I will start with what I am most familiar with.

The focus here is on packaging and not dicussing source code, in short I have an app named add_app which adds two numbers which contains a test for that function.

## [Setuptools](https://setuptools.pypa.io/en/latest/index.html)

```
Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects.

It helps developers to easily share reusable code (in the form of a library) and programs (e.g., CLI/GUI tools implemented in Python), that can be installed with pip and uploaded to PyPI.
```

We will be using this tool to package our project. Please visit there website to learn more.

# Packaging our app

## setup.py

Let's get started packaging our app. We're going to create a setup.py within the `add_app/` folder then we will add data to it.

1. `touch setup.py`
2. Add the following data.

```
from setuptools import setup

setup(name='add_app',
      version='0.1',
      description='An app that adds!',
      url='https://fakeurl.com',
      author='Foo Bar',
      author_email='foo.bar@foo.com',
      license='MIT',
      packages=['add_app'],
      zip_safe=False)
```

This is metadata which encapsulates the package you are creating.  Go to [setuptools](https://github.com/pypa/setuptools) to learn more about the different meta data items you can potentially add.

## Installing locally

