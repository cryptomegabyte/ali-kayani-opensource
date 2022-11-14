from app.factorial import factorial
import pytest

"""
Tests for factorial function

Behaviours
1. Should calculate the correct factorial given a number
"""

@pytest.mark.parametrize("number,result", [(4,24),(0,1),(5,120)])
def test_factorial(number: int, result: int) -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = factorial(number)

    # then
    assert test_wrapper == result
