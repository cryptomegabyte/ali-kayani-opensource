from functions.pack import pack

# Behviours:

# 1. Unpack a tuple to return a,b


def test_pack() -> None:
    """
    Tests demonstrating how to unpack tuples
    """    
    # given
    test_wrapper = None
    test_data = (1,2)

    # when
    test_wrapper = tuple_unpack(test_data)
    a, b = test_wrapper
    
    # then
    assert a == 1
    assert b == 2