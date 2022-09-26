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

# Behviours:

# 1. Unpack a tuple to return a,b

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
def list_unpack(data: list) -> tuple[int,int]:
    """
    Demonstrates unpacking of a list
    """
    a,b = data
    return a,b
```

Here we are simply unpacking the list data which is equal to `[1,2]` and assigning it variables a and b which we then return.

`a,b = [1,2]`. a = 1 and b = 2. simple enough.

We can also unpack dictionaries.

## test_dict_unpack

Add the following code to the file and run pytest `pytest`. The test should fail.

```python
from functions.dict_unpack import dict_unpack

# Behviours:

# 1. Unpack the keys of a dictionary
# 2. Unpack the values of a dictionary
# 3. Unpack the key value 


def test_dict_unpack() -> None:
    """
    Tests demonstrating how to unpack tuples
    """    
    # given
    test_wrapper = None
    test_data = {
        'a': 1,
        'b': 2
    }

    # when
    test_wrapper = dict_unpack(test_data,'keys')
    a, b = test_wrapper
    
    # then
    assert a == 'a'
    assert b == 'b'

    # when
    test_wrapper = dict_unpack(test_data,'values')
    a, b = test_wrapper
    
    # then
    assert a == 1
    assert b == 2

    # when
    test_wrapper = dict_unpack(test_data,'items')
    a, b = test_wrapper
    
    # then
    assert a == ('a',1)
    assert b == ('b',2)

```

## dict_unpack.py

Add the following code to the file and run pytest `pytest`. The test should pass.

```python
def dict_unpack(data: dict, operation: str) -> tuple[any,any]:
    """
    Demonstrates unpacking of a dict
    """
    match operation:
        case 'keys':
            a,b = data
            return a,b
        case 'values':
            a,b = data.values()
            return a,b
        case 'items':
            a,b = data.items()
            return a,b
```

