# Packaging

Installing python packages with pip is simple enough, `python -m pip install <package_name>` and the package is installed for you. As a seasoned software engineer who works with python I wanted to dive a little deeper into the world of packaging, this article is an attempt to uncover how python projects can be packaged for distribution.

# Sample Project

I will be using a small calculator project to demonstrate the concept of packaging an app. This isn't the only way that you can package a python app, I will be discussing how you can package an app with `poetry` to, but first, I will start with what I am most familiar with.

The focus here is on packaging and not dicussing source code, in short I have an app named add_app which adds two numbers which contains a test for that function.

