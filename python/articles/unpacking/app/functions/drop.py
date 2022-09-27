def drop(data: tuple) -> tuple[any,any]:
    """
    Demonstrates dropping of data using *_
    """
    a
    a,*_ = data
    return a,_