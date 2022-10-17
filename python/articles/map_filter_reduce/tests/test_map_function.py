import pytest
from src.map_function import map_function
"""
Tests for the map function

Behaviours:

1. Should produce a list of squared numbers
"""

def test_map_function() -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = map_function([1,2,3,4,5])

    # then
    assert test_wrapper == [1,2,9,16,25]