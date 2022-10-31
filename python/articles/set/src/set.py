from typing import Iterable


def set_function(x: Iterable) -> set:
    """
    Creates a set and returns it
    Input: iterable
    Output: set
    """
    return set(x)

def set_function_union(x: Iterable, y: Iterable) -> set:
    """
    Creates a set and returns it
    Input: iterable
    Output: set of all elements
    """
    return x.union(y) # can also be done like this: x | y

def set_function_intersection(x: Iterable, y: Iterable) -> set:
    """
    Creates a set and returns it
    Input: iterable
    Output: set - elements common to both sets
    """
    return x.intersection(y) # can also be done like this: x & y

def set_function_difference(x: Iterable, y: Iterable) -> set:
    """
    Creates a set and returns it
    Input: iterable
    Output: set - elements in x but not in y
    """
    return x.difference(y) # can also be done like this: x - y