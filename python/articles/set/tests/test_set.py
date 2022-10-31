from src.set import (
    set_function,
    set_function_union,
    set_function_intersection,
    set_function_difference
)
"""
Tests for sets.
Behaviours:
1. Should create a set from an iterable and return it.
"""

def test_set_function() -> None:
    
    # Given
    test_wrapper = None

    # When
    test_wrapper = set_function({})

    # then
    assert type(test_wrapper) is set

    # When
    test_wrapper = set_function([1,2,3,4])

    # then
    assert type(test_wrapper) is set

    # When
    test_wrapper = set_function([1,2,3,4])

    # then
    assert bool(test_wrapper) is True

    # When
    test_wrapper = set_function({})

    # then
    assert bool(test_wrapper) is False

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

    # When
    test_wrapper = set_function_union({1,2,3,4,5},{6,7,8,9,10})

    # then
    assert test_wrapper == {1,2,3,4,5,6,7,8,9,10}

    # When
    test_wrapper = set_function_intersection({1,2,3,4,5},{3,4,5,6,7,8,9,10})

    # then
    assert test_wrapper == {3,4,5}

    # When
    test_wrapper = set_function_difference({1,2,3,4,5},{3,4,5,6,7,8,9,10,11})

    # then
    assert test_wrapper == {1,2}