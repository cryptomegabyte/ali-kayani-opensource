# *args & **kwargs

Are you a fan of warhammer 40k? If you haven't heard of it, don't worry, I was simply going to say that `args` and `kwargs` is something that an `ork` might say `waaagh` (google that if you need to lol).

In order to understand `args` & `kwargs` let's dive into an example.

# *args
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

Install the requirements: `python -m pip install -r requirements.txt`.

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
  (2, 3, 4, 9)
=================================== short test summary info ====================================
ERROR app/tests/test_sum.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!
======================================= 1 error in 0.04s =======================================
```

What's happened? We sent in `(2,3,4)` and we expected the function to add it, but it didn't. The function definition itself expects two arguments, not three. Is there a way we could make the function work no matter how many inputs we provide?

Short answer: `yes`!

Let's start by modifying our test.

## test_sum.py

```python
import pytest
from src.sum import sum

@pytest.mark.parametrize("numbers,result",[((5,2),7),((7,7),14),((2,3,4),9)])
def test_sum(numbers: tuple, result: int) -> None:
    """
    Tests the sum function
    """

    # given
    test_wrapper = None

    # when
    test_wrapper = sum(*numbers)

    # then
    assert test_wrapper == result

```

# sum.py

```python
def sum(*numbers: tuple) -> int:
    """
    Adds numbers
    Input:
        numbers: tuple
    Output:
        int: sum
    """
    total = 0

    for number in numbers:
        total += number

    return total

```

Run `pytest` and the tests should pass. What we have done is to modify the function behaviour to take in an unlimited amount of arguments. 

Take a close look at the function definition `def sum(*numbers: tuple) -> int:`. I am passing in a tuple called numbers with an asterix pre-fixed to it. 

Take note that the name does not matter, I could change the function definition to `def sum(*args: tuple) -> int:` and the code would work the same, normally, engineers do just that. The name does not matter it's the `*` that does.

# **kwargs

We've seen how we can sent a variable number of arguments into a function that is determined at runtime, now we're going to look at how we can send in a variable numbers of `keyword arguments` (kwargs) into a function.

The name `kwargs` is not important. I can name it `person` if I wanted, what is important is the double asterisk `**`.

Let's add a function to our app which accepts a name and a phone number and returns it.

```
app/
|---src/
|-----__init__.py
|-----sum.py
|-----phone_book.py <<< create >>>
|---tests
|-----__init__.py
|-----test_sum.py
|-----test_phone_book.py <<< create >>>
|---requirements.txt
```

## test_phone_book.py

```python
from src.phone_book import phone_book

"""
As a software engineer I need to write a function
Which returns a dict consisting of a persons name and phone number.

"""

def test_phone_book() -> None:

    # given
    test_wrapper = None
    
    # when
    test_wrapper = phone_book(name="John Doe", phone_numer="00000000")

    # then
    assert test_wrapper == {
        "name": "John Doe",
        "phone_number": "00000000",

    }
```

## phone_book.py

```python
def phone_book(name: str = "", phone_numer: str ="") -> dict:
    """
    A function which returns a phone book
    Input:
        name: str: Persons name
        phone_number: str: Phone number
    Returns:
        phone_book: dict
    """

    return {
        "name": name,
        "phone_number": phone_numer
    }
```

Run `pytest` the test passes. We want to add an address field to our phonebook record, we will have to update the test and then the code. Let's do that.

## test_phone_book.py

```python
from src.phone_book import phone_book

"""
As a software engineer I need to write a function
Which returns a dict consisting of a persons name and phone number.

"""

def test_phone_book() -> None:

    # given
    test_wrapper = None
    
    # when
    test_wrapper = phone_book(name="John Doe", phone_numer="00000000", address="Test address")

    # then
    assert test_wrapper == {
        "name": "John Doe",
        "phone_number": "00000000",
        "address": "Test address"
    }
```

## phone_book.py

```python
def phone_book(name: str = "", phone_numer: str ="", address="") -> dict:
    """
    A function which returns a phone book
    Input:
        name: str: Persons name
        phone_number: str: Phone number
    Returns:
        phone_book: dict
    """

    return {
        "name": name,
        "phone_number": phone_numer,
        "address": address
    }
```
Run `pytest` the test passes. If we wanted to add an `email` field we would need to follow the same steps. It can get quite repetitive, luckily enough `**` to the rescue.

We can define as many fields as we want without having to define it in our function definition.

Modify the test and code as shown.

## test_phone_book.py

```python
from src.phone_book import phone_book

"""
As a software engineer I need to write a function
Which returns a dict consisting of a persons name and phone number.

"""

def test_phone_book() -> None:

    test_person = {
        "name": "John Doe",
        "phone_number": "00000000",
        "address": "Test address"
    }

    # given
    test_wrapper = None
    
    # when
    test_wrapper = phone_book(**test_person)

    # then
    assert test_wrapper == test_person

```

## phone_book.py

```python
def phone_book(**person) -> dict:
    """
    A function which returns a phone book
    Input:
        name: str: Persons name
        phone_number: str: Phone number
    Returns:
        phone_book: dict
    """

    return {
        **person
    }
```

Run `pytest` the test passes. Notice how I am using `**` in my test and code. I will now prove to you that it doesn't matter what attribute our person has, the function will always return a phone book record of their details without modification of the function definition.

Modify the test:

```python
import pytest
from src.phone_book import phone_book

"""
As a software engineer I need to write a function
Which returns a dict consisting of a persons name and phone number.

"""

test_phone_book_data = [
    {
        "name": "John Doe",
        "phone_number": "00000000",
        "address": "Test address"
    },
    {
        "name": "John Doe's Wife",
        "phone_number": "00000001",
        "address": "Test address",
        "email": "test@test.com"
    },
]

@pytest.mark.parametrize("test_person,phone_record",[(test_phone_book_data[0],test_phone_book_data[0]),(test_phone_book_data[1],test_phone_book_data[1])])
def test_phone_book(test_person, phone_record) -> None:

    # given
    test_wrapper = None
    
    # when
    test_wrapper = phone_book(**test_person)

    # then
    assert test_wrapper == phone_record


```

Notice that the second person in the list has an email field. Run `pytest` and the test should pass. 

This means that like `args` we can send a variable number of keyword arguments into a function at runtime without explicity having to define what they are.  Powerful behaviour.

## Conclusion

We've seen practial test driven examples of how we can use kwargs and args to pass in a variable number of arguments at runtime.

You can continue to pass in `standard` arguments into a function along with kwargs and args.

```python
def example_function(alpha, beta, *args, **kwargs):
```
Standard arguments (alpha, beta) have to be defined first, then `*args` and finally `**kwargs`.
