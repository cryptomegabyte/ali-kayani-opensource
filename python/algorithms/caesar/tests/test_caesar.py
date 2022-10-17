from src.caesar import caesar
import pytest

"""
Tests for caesar function

Behaviours:
- Should receive a string
- Encode the string
- Return the encoded string

"""

@pytest.mark.parametrize("message,encoded_string",[(".","."),("hello","khoor"),("Hello World!","Hhoor Wruog!")])
def test_caesar(message: str, encoded_string: str) -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = caesar(message)

    # then
    assert test_wrapper == encoded_string