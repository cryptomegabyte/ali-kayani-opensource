from functions.merge import merge
import pytest

# Behviours:

# 1. Merge a tuple

# @pytest.mark.parametrize("data,data,result",[()])
def test_merge() -> None:
    """
    Tests demonstrating how to merge using *
    """    
    # given
    test_wrapper = None
    test_data_a = (1,2,3)
    test_data_b = (4,5,6)

    # when
    test_wrapper = merge(test_data_a, test_data_b)
    
    # then
    assert test_wrapper == (*test_data_a,*test_data_b)
