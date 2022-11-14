from src.app.factorial import factorial

"""
Tests for factorial function

Behaviours
1. Should calculate the correct factorial given a number
"""

def test_factorial() -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = factorial(4)

    # then
    assert test_wrapper == 24