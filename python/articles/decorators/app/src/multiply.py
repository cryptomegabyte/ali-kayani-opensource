from src.decorator import decorator

@decorator
def multiply(x: int, y:int) -> int:
    return x * y

