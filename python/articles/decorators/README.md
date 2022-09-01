# Python Decorators

I first encountered decroators when I was loooking for a simple way to add open elemetry to a python project. I was familiar with the theory but I actually never had to use them in practice.

The project itself was rather large, altering every function would involve a lot of work, I needed a simple solution to drop into the project which wouldn't fail tests as well as adding the new telemetry logic, decorators to the rescue.

## What are decorators?

In short they are higher order functions. It's a function that takes in another function and extends it's behaviour without modifying it.

