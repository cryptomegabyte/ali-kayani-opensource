import pytest
from src.loops import loops

"""
For all non-negative integers i < n, print i**2.
1 <= n <= 20
"""

@pytest.mark.parametrize("x,result",[(5,[0,1,4,9,16])])
def test_loops(x: int, result: list) -> list:

    """
    Tests the loops function
    """

    # given
    test_wrapper = None

    # when
    test_wrapper = loops(x)

    # then
    assert test_wrapper == result