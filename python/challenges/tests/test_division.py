import pytest
from src.division import division

"""
The first line should contain the result of integer division,  a//b . 
The second line should contain the result of float division,  a/b .

No rounding or formatting is necessary.

Example


The result of the integer division 3/5 = 0.
The result of the float division is 3/5 = 0.6.

"""

@pytest.mark.parametrize("x,y,result",[(3,5,(0,0.6)),(5,3,(1,1.6666666666666667)),(50,100,(0,0.5))])
def test_division(x:int,y:int,result:tuple) -> None:
    
    # given
    test_wrapper = None

    # when
    test_wrapper = division(x,y)

    # then
    assert test_wrapper == result
