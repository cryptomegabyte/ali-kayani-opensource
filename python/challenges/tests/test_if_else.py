from xml.dom import ValidationErr
import pytest 

from src.if_else import IfElse

"""
Given an integer,n, perform the following conditional actions:

If n is odd, print odd
If n is even and in the inclusive range of 2 to 5, print Not odd
If n is even and in the inclusive range of 6 to 20, print odd
If n is even and greater than 20, print Not odd

Contraints: 1 =< n >= 100

"""

@pytest.mark.parametrize("input,output", [(3,"odd"),(4,"Not odd"),(12,"odd"),(32, "Not odd")])
def test_if_else(input,output) -> None:

    # given
    test_wrapper = None

    # when
    test_wrapper = IfElse(input)

    # then
    assert test_wrapper == output


@pytest.mark.parametrize("input,output", [(0,"out of bounds"),(202,"out of bounds")])
def test_recursion_depth(input,output):
    with pytest.raises(ValueError) as excinfo:
        IfElse(input)
    assert output == str(excinfo.value)