from app.binary_search import binary_search
import pytest

"""
Tests for binary search function

Behaviours:

1. Should return index of search item.
2. Should return a -1 if not found
"""
@pytest.mark.parametrize("x,y,r",[([4],4,0),([1,2,3,4,5],3,2),([1,2,3,4,5],6,-1)])
def test_binary_search(x: list[int], y: int, r: int) -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = binary_search(x,y)

    # then
    assert test_wrapper == r
