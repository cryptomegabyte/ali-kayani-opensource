from typing import Callable
import functools


def decorator(func: Callable) -> None:
    @functools.wraps(func)
    def inner_wrapper(*args, **kwargs):
        print("Telemetry: The function is starting")
        result = func(*args, **kwargs)
        print("Telemetry: The function has executed")
        return result
    return inner_wrapper