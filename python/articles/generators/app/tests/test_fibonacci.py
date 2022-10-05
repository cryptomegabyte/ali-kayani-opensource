from src.fibonacci import fibonacci

# Behaviours
# 1. Should calculate the fib sequence given a integer

def test_fibonacci() -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = fibonacci(5)

    # then
    assert test_wrapper == [0,1,1,2,3]