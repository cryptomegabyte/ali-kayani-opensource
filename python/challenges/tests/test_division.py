from division import division

"""
The first line should contain the result of integer division,  a//b . 
The second line should contain the result of float division,  a/b .

No rounding or formatting is necessary.

Example


The result of the integer division 3/5 = 0.
The result of the float division is 3/5 = 0.6.

"""

def test_division() -> None:
    
    # given
    test_wrapper = None

    # when
    test_wrapper = division()

    # then
    assert test_wrapper == (0,3.5)