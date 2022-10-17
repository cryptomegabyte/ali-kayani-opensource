from src.map_function import (
    map_function_a,
    map_function_b,
    map_function_c,
    map_function_d
)
"""
Tests for the map function

Behaviours:

1. Should produce a list of squared numbers
2. Should convert a list of string numbers into ints
3. Should convert a list of negative numbers into positive ones
4. Should convert a list of ints tp floats
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

    # when
    test_wrapper = map_function_c([-10,-9,-8,-7,-6,-5])

    # then
    assert test_wrapper == [10,9,8,7,6,5]

    # when
    test_wrapper = map_function_d([1,2,3,4,5])

    # then
    assert test_wrapper == [1.0,2.0,3.0,4.0,5.0]


