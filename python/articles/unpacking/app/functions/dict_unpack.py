def dict_unpack(data: dict, operation: str) -> tuple[any,any]:
    """
    Demonstrates unpacking of a dict
    """
    match operation:
        case 'keys':
            a,b = data
            return a,b
        case 'values':
            a,b = data.values()
            return a,b
        case 'items':
            a,b = data.items()
            return a,b
