import pytest
from src.arithmetic import arithmetic

"""
Given two numbers a,b.

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""

@pytest.mark.parametrize("x,y,result",[(3,5,(8,-2,15)),(3,2,(5,1,6))])
def test_arithmetic(x,y,result) -> None:
    test_wrapper = arithmetic(x,y)

    assert test_wrapper == result