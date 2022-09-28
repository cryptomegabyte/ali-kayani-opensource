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

Based on what type of data we want to select (keys, values or key-value pairs) we can unpack that data and return it.

## Packing

We've looked at unpacking, let's now take a look at Packing itself. I think of the * operator as the unpacking operator but it can be used for quite the opposite. It can also be used to collect variables.

Let's take a look at how it can be used to `pack` items.

## test_pack.py

Add the following code to the file and run pytest `pytest`. The test should fail.

```python
from functions.pack import pack

# Behviours:

# 1. Pack a tuple
# 2. Pack a list

def test_pack() -> None:
    """
    Tests demonstrating how to pack using *
    """    
    # given
    test_wrapper = None
    test_data = (1,2,3)

    # when
    test_wrapper = pack(test_data)
    a, b = test_wrapper
    
    # then
    assert a == [1,2]
    assert b == 3

    # given
    test_data_list = [1,2,3]

    # when
    test_wrapper = pack(test_data_list)
    a, b = test_wrapper
    
    # then
    assert a == [1,2]
    assert b == 3
```

## pack.py

Add the following code to the file and run pytest `pytest`. The test should pass.

```python
def pack(data: any) -> tuple[any,any]:
    """
    Demonstrates the use of packing operator *
    """
    *a,b = data
    return a,b
```

The * operator can be used to gather data.

We have some data, let's say `(1,2,3.2,3.3,4.5)`, there is a requirement to drop the data after the first number. We could devise an algorithm that iterates through the tuple, detects the numbers after the first then removes them, we also can used the `*` operator to quickly drop the data we don't want, let see how.

## test_drop.py

Add the following code to the file and run pytest `pytest`. The test should fail.

```python
from functions.drop import drop

# Behviours:

# 1. Drop data.


def test_drop() -> None:
    """
    Tests demonstrating how to unpack lists
    """    
    # given
    test_wrapper = None
    test_data = (1,2,3.2,3.3,4.5)

    # when
    test_wrapper = drop(test_data)
    a, _ = test_wrapper
    
    # then
    assert a == 1
    assert _ == [2,3.2,3.3,4.5]

```

## drop.py

Add the following code to the file and run pytest `pytest`. The test should pass.

```python
def drop(data: tuple) -> tuple[any,any]:
    """
    Demonstrates dropping of data using *_
    """
    a
    a,*_ = data
    return a,_
```

Here we unpack the first result and the rest we unpack using `*_`. Off course we could also have done `a[0]` to get the first item from the tuple.

Let's look at how we can merge using the `*` operator.

## test_merge.py

Add the following code to the file and run pytest `pytest`. The test should fail.

```python
from functions.merge import merge,merge_list

# Behviours:

# 1. Merge a tuple

def test_merge() -> None:
    """
    Tests demonstrating how to merge using *.
    """    
    # given
    test_wrapper = None
    test_data_a = (1,2,3)
    test_data_b = (4,5,6)

    # when
    test_wrapper = merge(test_data_a, test_data_b)
    
    # then
    assert test_wrapper == (*test_data_a,*test_data_b)

def test_merge_list() -> None:
    """
    Tests demonstrating how to merge using *, transforming into list.
    """    
    # given
    test_wrapper = None
    test_data_a = (1,2,3)
    test_data_b = (4,5,6)

    # when
    test_wrapper = merge_list(test_data_a, test_data_b)
    
    # then
    assert test_wrapper == [*test_data_a,*test_data_b]
```

## merge.py

Add the following code to the file and run pytest `pytest`. The test should pass.

```python
def merge(data_a: tuple, data_b: tuple) -> tuple:
    """
    Demonstrates the use of packing operator * to merge.
    """
    merged = (*data_a,*data_b)
    return merged

def merge_list(data_a: tuple, data_b: tuple) -> list:
    """
    Demonstrates the use of packing operator * to merge list
    """
    merged_list = [*data_a,*data_b]
    return merged_list

```

The above is an example of how we can merge tuples to for a larger tuple or list.

Now let's take a look at the unpacking dictionaries using `**`. Let's say you have a persons details, for arguments sake their name, phone and email. You wanted to form a phone book which consists of many people. We can use the `**` unpacking operator to merge dictionaries.

Let's take a look at an example of how we can do that.

This is the data that we will hold in the dictionary:

```
| Name | Phone | E-mail |
| Homer Simpson | 056375863 | homer.s@simpsons.com |
| Wyatt Earp | 896832456 | wyatt.e@outlaw.com |
```

## test_phonebook.py

Add the following code to the file and run pytest `pytest`. The test should fail.

```python

from functions.phonebook import phonebook

# Behviours:

# 1. Merge a dictionary

def test_merge() -> None:
    """
    Tests demonstrating how to merge using **
    """    
    # given
    test_wrapper = None

    test_person_a = {
        'name_a': 'Homer Simpson',
        'phone_a': '056375863',
        'email_a': 'homer.s@simpsons.com'
    }
    test_person_b = {
        'name_b': 'Wyatt Earp',
        'phone_b': '896832456 ',
        'email_b': 'wyatt.e@outlaw.com'
    }

    # when
    test_wrapper = phonebook(test_person_a, test_person_b)
    
    # then
    assert test_wrapper == {
        **test_person_a,
        **test_person_b
    }

```

## phonebook.py

Add the following code to the file and run pytest `pytest`. The test should pass.

```python
def phonebook(person_a: dict, person_b: dict ) -> dict:
    """
    Demonstrates the use of unpacking dicts using **
    """
    return {
        **person_a,
        **person_b
    }

```

It's quite simple to merge dictionaries as you can see from the above example. Do keep in mind that the keys will have to be unique, if not they will be overridden by the last value.

One last point, in the example below I have shown how you can unpack within a foor loop.

```python

phonebook = [
    ('Arnold S', '07646569007'),
    ('Jerry R', '873658766'),
]

for name,phone in phonebook:
    print(f"{name}: {phone}")

```

You can do the same with dictionaries.  

# Summary

Unpacking is a powerful technique that can simply a complex problem. I have shown how it can be used in a number of different scenarios.