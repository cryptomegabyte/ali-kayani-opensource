from typing import Callable


def decorator(func: Callable) -> None:
    def inner_wrapper(*args, **kwargs):
        print("Telemetry: The function is starting")
        result = func(*args, **kwargs)
        print("Telemetry: The function has executed")
        return result
    return inner_wrapper