def sum(*numbers: tuple) -> int:
    """
    Adds numbers
    Input:
        numbers: tuple
    Output:
        int: sum
    """
    total = 0

    for number in numbers:
        total += number

    return total
