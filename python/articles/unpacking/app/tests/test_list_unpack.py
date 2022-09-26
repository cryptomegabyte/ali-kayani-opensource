from functions.list_unpack import list_unpack

# Behviours:

# 1. Unpack a list to return a,b


def test_tuple_unpack() -> None:
    """
    Tests demonstrating how to unpack tuples
    """    
    # given
    test_wrapper = None
    test_data = [1,2]

    # when
    test_wrapper = list_unpack(test_data)
    a, b = test_wrapper
    
    # then
    assert a == 1
    assert b == 2