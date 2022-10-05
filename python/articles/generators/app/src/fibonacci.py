def fibonacci(x:int) -> list:
    """
    Calculates the fib sequence given a integer
    input:
        x: int
    output:
        result: list of fib numbers
    """
    a = 0
    b = 1
    result = []

    for number in range(x):
        result.append(a)
        a,b = b, a+b
    return result