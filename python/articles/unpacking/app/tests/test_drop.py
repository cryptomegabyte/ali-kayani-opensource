from functions.drop import drop

# Behviours:

# 1. Drop data.


def test_drop() -> None:
    """
    Tests demonstrating how to unpack lists
    """    
    # given
    test_wrapper = None
    test_data = (1,2,3.2,3.3,4.5)

    # when
    test_wrapper = drop(test_data)
    a, _ = test_wrapper
    
    # then
    assert a == 1
    assert _ == [2,3.2,3.3,4.5]
