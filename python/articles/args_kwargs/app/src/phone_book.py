def phone_book(**person: dict) -> dict:
    """
    A function which returns a phone book
    Input:
        name: str: Persons name
        phone_number: str: Phone number
    Returns:
        phone_book: dict
    """

    return {
        **person
    }
