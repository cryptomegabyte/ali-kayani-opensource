def IfElse(n: int) -> str:

    if ( n < 1 or n > 100 ):
        raise ValueError("out of bounds")

    odd_even = "even"

    if n % 2:
        odd_even = "odd"
        return odd_even
    
    if (odd_even == "even" and n >= 2 and n <= 5 ):
        return "Not odd"
    
    if (odd_even == "even" and n >= 6 and n <= 20 ):
        return "odd"

    if (odd_even == "even" and n > 20 ):
        return "Not odd"
