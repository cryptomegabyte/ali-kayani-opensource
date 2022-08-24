# Packaging

Installing python packages with pip is simple enough, `python -m pip install <package_name>` and the package is installed for you. As a seasoned software engineer who works with python I wanted to dive a little deeper into the world of packaging, this article is an attempt to uncover how python projects can be packaged for distribution.

## Sample Project

I will be using a small calculator project to demonstrate the concept of packaging an app. There are different versions of the app which start with a `v`, as I progress through the article it will become apparent why I have named them this way.

