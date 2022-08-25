import pytest
from src.add import add

@pytest.mark.parametrize("x,y,result",[(1,2,3), (4,5,9), (6,7,13)])
def test_add(x:int, y:int, result:int) -> None:

    # given
    test_wrapper = None
    # when
    test_wrapper = add(x,y)
    # then
    assert test_wrapper == result

