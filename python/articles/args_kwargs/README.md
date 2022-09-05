# *args & **kwargs

Are you a fan of warhammer 40k? If you haven't heard of it, don't worry, I was simply going to say that `args` and `kwargs` is something that an `ork` might say `waaagh` (google that if you need to lol).

In order to understand `args` & `kwargs` let's dive into an example.

## App

Create an `app/` folder and add the follwing structure.

```
app/
|---src/
|-----__init__.py
|-----sum.py
|---tests
|-----__init__.py
|-----test_sum.py
|---requirements.txt
```

## requirements.txt

Copy the follwing into the requirements.txt file.

```python
pytest
```

Create a virtual enviornment: `python -m venv venv`.

Activate the virtual environment: `. venv/bin/activate`.

Install the requirments: `python -m pip install -r requirements.txt`.

## test_sum.py

Add the following code to test_sum.py

```python
from src.sum import sum

def test_sum() -> None:
    """
    Tests the sum function
    """

    # given
    test_wrapper = None

    # when
    test_wrapper = sum(5,2)

    # then

    assert test_wrapper == 7
```

Here we have a test which tests to see if the output of the sum function equals `7`.

## sum.py

Add the following code to sum.py

```python
def sum(x: int, y:int) -> int:
    """
    Adds numbers
    Input:
        x: int
        y: int
    Output:
        int: sum
    """
    return x + y
```

From the `app/`directory run `pytest`. The test should pass.  Let's add more tests to test our function. We're going to be using [pytest parametrize](https://docs.pytest.org/en/6.2.x/parametrize.html) to send in more test data to the sum function.

## test_sum.py

```python



```