from functions.pack import pack

# Behviours:

# 1. Pack a tuple
# 2. Pack a list

def test_pack() -> None:
    """
    Tests demonstrating how to pack using *
    """    
    # given
    test_wrapper = None
    test_data = (1,2,3)

    # when
    test_wrapper = pack(test_data)
    a, b = test_wrapper
    
    # then
    assert a == [1,2]
    assert b == 3

    # given
    test_data_list = [1,2,3]

    # when
    test_wrapper = pack(test_data)
    a, b = test_wrapper
    
    # then
    assert a == [1,2]
    assert b == 3

