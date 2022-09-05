from src.sum import sum

def test_sum() -> None:
    """
    Tests the sum function
    """

    # given
    test_wrapper = None;

    # when
    test_wrapper = sum(5,2)

    # then

    assert test_wrapper == 7