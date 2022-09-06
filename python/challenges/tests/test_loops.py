from src.loops import loops

"""
For all non-negative integers i < n, print i**2.
1 <= n <= 20
"""

def test_loops(n: int) -> list:

    """
    Tests the loops function
    """

    # given
    test_wrapper = None

    # when
    test_wrapper = loops(5)

    # then
    assert test_wrapper == [0,1,4,9,16]