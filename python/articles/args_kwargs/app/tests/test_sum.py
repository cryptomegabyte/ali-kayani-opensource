import pytest
from src.sum import sum

@pytest.mark.parametrize("numbers,result",[((5,2),7),((7,7),14),((2,3,4),9)])
def test_sum(numbers: tuple, result: int) -> None:
    """
    Tests the sum function
    """

    # given
    test_wrapper = None

    # when
    test_wrapper = sum(*numbers)

    # then
    assert test_wrapper == result
