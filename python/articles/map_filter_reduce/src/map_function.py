"""
map(function, iterable[, iterable1, iterable2,..., iterableN])

"""

def map_function_a(numbers: list[int]) -> list[int]:
    """
    map function: raise to the power of each number
    input:
      numbers: list: list of numbers
    return:
      list: list of powered numbers
    """
    return list(map(lambda x: x**x, numbers))

def map_function_b(string_numbers: list[str]) -> list[int]:
    """
    map function: converts strings to ints
    input:
      numbers: list: list of numbers
    return:
      list: list of ints
    """

    return list(map(int, string_numbers))

def map_function_c(string_numbers: list[int]) -> list[int]:
    """
    map function: converts negative ints to abs ints
    input:
      numbers: list: list of numbers
    return:
      list: absolute numbers
    """

    return list(map(abs, string_numbers))

def map_function_d(string_numbers: list[int]) -> list[float]:
    """
    map function: converts strings to ints
    input:
      numbers: list: list of numbers
    return:
      list: absolute numbers
    """

    return list(map(float, string_numbers))
