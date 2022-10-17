def map_function(numbers: list) -> list[int]:
    squared_numbers = list(map(lambda x: x**x, numbers))
    return squared_numbers