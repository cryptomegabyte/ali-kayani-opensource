from src.fib_gen import fib_gen

# Behaviours
# 1. Should calculate the fib sequence given a integer

def test_fib_gen() -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = fib_gen(5)
    
    # then
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 0
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 1
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 1
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 2
    test_fib_value = next(test_wrapper)
    assert test_fib_value == 3

