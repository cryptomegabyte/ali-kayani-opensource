
from src.multiply import multiply
from src.decorator import decorator

def test_decorator() -> None:

    # given
    test_wrapper = None

    # when
    test_wrapper = decorator(multiply)

    # then
    assert test_wrapper == 50