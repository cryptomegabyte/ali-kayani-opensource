# Unpacking

In my article on [args_kwargs](../args_kwargs/) we could looked at the * and ** operators and how they can be used. In this article I am going to closely look once again at the * and ** operators from a slightly different perspective.

# Tuple Unpacking

Tuples can be unpacked quite quickly, let's set up an app, as always we will write tests first then write the accompanying code.

## App

Create the following app structure

```
app/
|--tests/
|----__init__.py
|----test_tuple_unpack.py
|--functions/
|-----tuple_unpack.py
|--requirements.txt
```

## Virtual environment

`python -m venv venv` will create a virtual environment.
`. venv/bin/activate` will activate that virtual environment.

## Requirements.txt

`echo "pytest" >> requirements.txt` will create the file and populate it. Alternatively just create the file manually and add pytest.

```bash
pytest
```

`python -m pip install -r requirements.txt` will install pytest.

## test_tuple_unpack.py

Add the following code to the file and run pytest `pytest`. The test should fail.

```python
from functions.tuple_unpack import tuple_unpack

def test_tuple_unpack() -> None:
    """
    Tests demonstrating how to unpack tuples
    """    
    # given
    test_wrapper = None
    test_data = (1,2)

    # when
    test_wrapper = tuple_unpack(test_data)
    a, b = test_wrapper
    
    # then
    assert a == 1
    assert b == 2
```

## tuple_unpack.py

Add the following code to the file and run pytest `pytest`. The test should pass.

```python
def tuple_unpack(data: tuple) -> tuple[int,int]:
    """
    Demonstrates unpacking of a tuple
    """
    a,b = data
    return a,b
```

Here we are simply unpacking the tuple data which is equal to `(1,2)` and assigning it variables a and b which we then return.

`a,b = (1,2)`. a = 1 and b = 2. simple enough.

We can do the same to lists, let's see how.

## test_list_unpack.py

Add the following code to the file and run pytest `pytest`. The test should fail.

```python
from functions.tuple_unpack import list_unpack

# Behviours:

# 1. Unpack a list to return a,b


def test_tuple_unpack() -> None:
    """
    Tests demonstrating how to unpack tuples
    """    
    # given
    test_wrapper = None
    test_data = [1,2]

    # when
    test_wrapper = list_unpack(test_data)
    a, b = test_wrapper
    
    # then
    assert a == 1
    assert b == 2
```

## list_unpack.py

Add the following code to the file and run pytest `pytest`. The test should pass.

```python
def list_unpack(data: tuple) -> tuple[int,int]:
    """
    Demonstrates unpacking of a list
    """
    a,b = data
    return a,b
```

Here we are simply unpacking the list data which is equal to `[1,2]` and assigning it variables a and b which we then return.

`a,b = [1,2]`. a = 1 and b = 2. simple enough.

