def drop(data: tuple) -> tuple[any,any]:
    """
    Demonstrates dropping of data using *_
    """
    a,*_ = data
    return a,_