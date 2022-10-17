import pytest
from src.map_function import (
    map_function_a,
    map_function_b
)
"""
Tests for the map function

Behaviours:

1. Should produce a list of squared numbers
"""

def test_map_functions() -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = map_function_a([1,2,3,4,5])

    # then
    assert test_wrapper == [1, 4, 27, 256, 3125]

    # when
    test_wrapper = map_function_b(["1","2","3","4","5"])

    # then
    assert test_wrapper == [1,2,3,4,5]