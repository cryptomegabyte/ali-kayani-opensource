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

def map_function_b(numbers: list[str]) -> list[int]:
    """
    map function: converts strings to ints
    input:
      numbers: list: list of numbers
    return:
      list: list of ints
    """

    return list(map(int, numbers))

def map_function_c(numbers: list[int]) -> list[int]:
    """
    map function: converts negative ints to abs ints
    input:
      numbers: list: list of numbers
    return:
      list: absolute numbers
    """

    return list(map(abs, numbers))

def map_function_d(numbers: list[int]) -> list[float]:
    """
    map function: converts strings to ints
    input:
      numbers: list: list of float numbers
    return:
      list: absolute numbers
    """

    return list(map(float, numbers))

def map_function_e(string_numbers: list[str]) -> list[int]:
    """
    map function: converts strings to ints
    input:
      numbers: list: list of numbers
    return:
      list: integer list of string lengths
    """

    return list(map(len, string_numbers))

def map_function_f(numbers_a: list[int], numbers_b: list[int]) -> list[int]:
    """
    map function: converts strings to ints
    input:
      numbers: list: list of numbers
    return:
      list: absolute numbers
    """

    return list(map(lambda x,y: x + y, numbers_a, numbers_b))