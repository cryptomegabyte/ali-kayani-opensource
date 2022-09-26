def pack(data: any) -> tuple[any,any]:
    """
    Demonstrates the use of packing operator *
    """
    *a,b = data
    return a,b