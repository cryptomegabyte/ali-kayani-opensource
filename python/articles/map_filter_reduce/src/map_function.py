"""
map(function, iterable[, iterable1, iterable2,..., iterableN])

"""

def map_function_a(numbers: list) -> list[int]:
    """
    map function: raise to the power of each number
    input:
      numbers: list: list of numbers
    return:
      list: list of powered numbers
    """
    return list(map(lambda x: x**x, numbers))