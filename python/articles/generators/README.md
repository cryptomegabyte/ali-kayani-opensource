# Generators

In computer science generators are used to control iteration behaviour of a loop. All generators are also iterators. Generators remember their internal state. Generators return interators.

That might be a bit of a mouthful, as always let's look at a practical example to aid our understanding.

# App

We're going to create an application that calculates the `fibonacci` sequence. If you don't know what the fibonacci sequence is, please use a search engine to look it up.

## Algorithm

- Define a function which takes in a number.
- Define two start values a,b. `a=0` `b=1`.
- Define an empty array called result.
- The number given to the function will be used to generate a sequence of integers.
- Iterate through that sequence. Within each iteration:
    - Add a to the result array
    - Change the value of a `a = b`.
    - Change the value of b `b = a + b`

## Folder structure

```bash
app/
|--tests/
|----__init__.py
|----test_fibonacci.py
|--src/
|----__init__.py
|----fibonacci.py
|--requirements.txt
```

## requirements.txt

Issue the follwing commands at the command prompt:

`echo "pytest" >> requirements.txt`
`python -m venv venv`
`. venv/bin/activate`
`python -m pip install -r requirements.txt`

The above commands will create a requirements file (if it does not exist), create a venv, activate the venv then finally install pytest.

## test_fibonacci.py

Add the following code then run `pytest` from the `app/` directory.

```python
from src.fibonacci import fibonacci

# Behaviours
# 1. Should calculate the fib sequence given a integer

def test_fibonacci() -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = fibonacci(5)

    # then
    assert test_wrapper == [0,1,1,2,3]

```

## fibonacci.py

Add the following code:

```python
def fibonacci(x:int) -> list:
    """
    Calculates the fib sequence given a integer
    input:
        x: int
    output:
        result: list of fib numbers
    """
    a = 0
    b = 1
    result = []

    for number in range(x):
        result.append(a)
        a,b = b, a+b
    return result
```

Run `pytest` and the test should pass.

Here we used 5 as an input which is a relatively small number. What if we wanted a rather large number, your computers memory would quickly fill up as it stores the whole fibonacci list. 

Generators are memory efficient. When used they can give back the result one number at a time. The whole list is not stored, we ask for a number and it is given to us.

Let's look at an example.

Add the following two files to the app

```bash
app/
|--tests/
|----__init__.py
|----test_fibonacci.py
|----test_fib_gen.py <<< add >>>
|--src/
|----__init__.py
|----fibonacci.py
|----fib_gen.py <<< add >>>
|--requirements.txt
```

## test_fib_gen.py

```python
from src.fib_gen import fib_gen

# Behaviours
# 1. Should calculate the fib sequence given a integer

def test_fib_gen() -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = fib_gen(5)
    
    # then
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 0
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 1
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 1
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 2
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 3

```

Run `pytest` and the test should fail.

## fib_gen.py

```python
from typing import Iterator


def fib_gen(x:int) -> Iterator[int]:
    """
    Calculates the fib sequence given a integer
    input:
        x: int
    output:
        result: list of fib numbers
    """
    a = 0
    b = 1

    for number in range(x):
        yield(a)
        a,b = b, a+b

```

Run `pytest` and the tests should pass.

You may have noticed a difference. Before in the original function I used `return`; return ends execution immediately and returns the list of values. `yield` pauses the function execution and returns a value. Notice in the test i am calling a `next` function.

This `next` function tells the function to give the next value. Simple. 

# Summary

Generators are much more memory efficient, they can be used in a wide variety of use cases to pause the execution of a function.