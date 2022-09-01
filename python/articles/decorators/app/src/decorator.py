from typing import Callable


def decorator(func: Callable) -> Callable:
    return func(5,10)