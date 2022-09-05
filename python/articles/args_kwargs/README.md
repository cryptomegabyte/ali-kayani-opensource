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

    assert test_wrapper == 
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

import pytest <<< new >>>
from src.sum import sum

@pytest.mark.parametrize("x,y,result",[(5,2,7)]) <<< new >>>
def test_sum(x:int, y:int, result:int) -> None:
    """
    Tests the sum function
    """

    # given
    test_wrapper = None

    # when
    test_wrapper = sum(x,y)

    # then

    assert test_wrapper == result

```

Run `pytest` and the test should pass. Let's add more data. Modify the following line:

```python
@pytest.mark.parametrize("x,y,result",[(5,2,7),(7,7,14)]) <<< modify >>>
```

Run `pytest` again and the test should pass.

Let's add one more set of data, like this:

```python
@pytest.mark.parametrize("x,y,result",[(5,2,7),(7,7,14),(2,3,4,9)])
```
Run `pytest` and the test should now fail.

```bash
____________________________ ERROR collecting app/tests/test_sum.py ____________________________
app/tests/test_sum.py::test_sum: in "parametrize" the number of names (3):
  ['x', 'y', 'result']
must be equal to the number of values (4):
  (2, 3, 4, 6)
=================================== short test summary info ====================================
ERROR app/tests/test_sum.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!
======================================= 1 error in 0.04s =======================================
```

What's happened? We sent in `(2,3,4)` and we expected the function to add it, but it didn't. The function definition itself expects two arguments, not three. Is there a way we could make the function work no matter how many inputs we provide?

Short answer: `yes`!