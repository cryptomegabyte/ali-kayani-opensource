from typing import Iterator


def fib_gen(x:int) -> Iterator[int]:
    """
    Calculates the fib sequence given a integer
    input:
        x: int
    return:
        value: yield fib number
    """
    a = 0
    b = 1

    for number in range(x):
        yield(a)
        a,b = b, a+b
