from functions.dict_unpack import dict_unpack

# Behviours:

# 1. Unpack the keys of a dictionary
# 2. Unpack the values of a dictionary
# 3. Unpack the key value 


def test_dict_unpack() -> None:
    """
    Tests demonstrating how to unpack tuples
    """    
    # given
    test_wrapper = None
    test_data = {
        'a': 1,
        'b': 2
    }

    # when
    test_wrapper = dict_unpack(test_data,'keys')
    a, b = test_wrapper
    
    # then
    assert a == 'a'
    assert b == 'b'

    # when
    test_wrapper = dict_unpack(test_data,'values')
    a, b = test_wrapper
    
    # then
    assert a == 1
    assert b == 2

    # when
    test_wrapper = dict_unpack(test_data,'items')
    a, b = test_wrapper
    
    # then
    assert a == ('a',1)
    assert b == ('b',2)
