def loops(x: int) -> list:
    
    """
    Squares a list is x > 0
    Input:
        x: int
    Output:
        list: Squared numbers or [0]
    """
    
    # Squared number list
    squared = []

    # If x is zero or a negative number just return 0
    if  x == 0 or x < 0:
        return [0]

    # Generate initial numbers
    numbers = list(range(x))

    # Use list comprehension to square numbers
    squared = [x**2 for x in numbers]

    # return squared numbers
    return squared
