from src.set import set_function
"""
Tests for sets.
Behaviours:
1. Should create a set from an list and retur it.
2. Should create a set of unique items and return it.
"""

def test_set_function() -> None:
    # Given
    test_wrapper = None

    # When
    test_wrapper = set_function([1,2,3,4])

    # then
    assert type(test_wrapper) is set

    # When
    test_wrapper = set_function([1,2,3,4,5,1,2,3,4,5])

    # then
    assert test_wrapper == {1,2,3,4,5}

    # When
    test_wrapper = set_function((1,2,3,4,5,1,2,3,4,5))

    # then
    assert test_wrapper == {1,2,3,4,5}

    # When
    test_wrapper = set_function("Hello")

    # then
    assert test_wrapper == {'H','e','l','l','o'}