import pytest
from src.sum import sum

@pytest.mark.parametrize("x,y,result",[(5,2,7),(7,7,14),(2,3,4,9)])
def test_sum(x:int, y:int, result:int) -> None:
    """
    Tests the sum function
    """

    # given
    test_wrapper = None

    # when
    test_wrapper = sum(x,y)

    # then

    assert test_wrapper == result