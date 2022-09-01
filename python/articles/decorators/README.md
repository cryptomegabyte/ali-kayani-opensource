# Python Decorators

I first encountered decroators when I was loooking for a simple way to add open telemetry to a python project. I was familiar with the theory but I actually never had to use them in practice.

The project itself was rather large, altering every function would involve a lot of work, I needed a simple solution to drop into the project which wouldn't fail tests as well as adding the new telemetry logic, decorators to the rescue.

## What are decorators?

In short they are higher order functions. It's a function that takes in another function and extends it's behaviour without modifying it.

# Example

I will demonstrate the concept of a decorator through an example.  Create a folder called app.

## Requirements.txt

Create a requirments.txt file in the `app/` folder and add the following text:

```
pytest
```

## venv

Create a virtual environment: `python -m venv venv`.

Activate the virtual environment: `. venv/bin/activate`

## Install dependencies

Install the items packages listed within the requirements file: `python -m pip install -r requirements.txt`

## Structure

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

Add the following to the multiply test file in `app/src/tests/`.

```python
import pytest

"""
Tests the multiplication function
"""

from src.multiply import multiply

@pytest.mark.parametrize("x,y,result",[(3,3,9),(8,8,64),(5,2,10)])
def test_multiply( x:int, y:int ,result:int ) -> None:
    
    # given
    test_wrapper = None

    # when
    test_wrapper = multiply(x,y)

    # then
    assert test_wrapper == result

```

## Multiply.py

Add the following to the multiply file in `app/src/`.

```python
def multiply(x: int, y:int) -> int:
    return x * y

```

Run the tests from the `app/` folder `pytest -v -rP` and they should pass. I don't think much explanation is needed as to what is happening here, I have a function that simply multiplies two numbers.

## Passing functions as arguments

Functions can be passed as arguments. For example `def a_function(another_function)`. Knowing this let's put together a function called decorator, which takes in a function.

```
app/
|---src/
|-----__init__.py
|-----multiply.py
|-----decorator.py
|---tests/
|-----__init__.py
|-----test_multiply.py
|-----test_decorator.py
```

## test_decorator.py

Add the following to the test decorator file under `app/tests/`.

```python
from src.multiply import multiply
from src.decorator import decorator

def test_decorator() -> None:

    # given
    test_wrapper = None

    # when
    test_wrapper = decorator(multiply)

    # then
    assert test_wrapper == 50
```

## Decorator.py

Add the following to the decorator file under `app/src/`

```python
from typing import Callable


def decorator(func: Callable) -> Callable:
    return func(5,10)
```

Run the tests from the `app/` folder `pytest -v -rP` and they should pass.

Here what we have done is taken a function and passed it into another function. Notice that I am calling the passed in function like so `func(5,10)`.

This isn't a great example of a decorator but it demonstrates the concept that a function can take in another function and call it.

Now we're going to develop the idea that functions can be nested in other functions. These are called closures.
## Closures

A closure encapsulates logic, everything from data through to other functions.

```python
def outer_function():

    global_variable = "Hello"

    def inner_function():
        local_variable = "World!"
        print(f"{global_variable} {local_variable}")
        return local_variable

    inner_function()

    return global_variable
```

```bash
>>> outer_function()
>>> "Hello World!"

```

The `inner_function` is locally scoped to the `outer_function` it only exists when the `outer_function` is called. The `outer_function` encapsulates all the other logic.

If you attempt to do this:

```bash
>>> inner_function()
```

You will get an error. The `inner_function` is scoped to the outer function and only exists when it does.

## Returning functions

As you have probably correctly deduced from reading the above, functions can also return other functions.

```python
def shape(letter):

    def square():
        return "I am a square"

    def triangle():
        return "I am a square"

    if letter == s:
        return square
    else:
        return triangle
```

```bash
>>> my_shape = shape(t)

```

What we are doing here is return a reference to a function based on a letter that we pass into the functon. In the above example we return a reference to the `triangle` function. Remember it only exists when the shape function is called.

```bash
>>> my_shape()
```

At this point you not be wrong in thinking that nesting functions like this is rather like developing classes. Remember that functions are first class objects.

