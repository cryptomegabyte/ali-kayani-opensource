import pytest

"""
Tests the multiplication function
"""

from src.multiply import multiply

@pytest.mark.parametrize("x,y,result",[(3,3,9),(8,8,64),(5,2,10)])
def test_multiply( x:int, y:int ,result:int ) -> None:
    
    # given
    test_wrapper = None

    # when
    test_wrapper = multiply(x,y)

    # then
    assert test_wrapper == result
