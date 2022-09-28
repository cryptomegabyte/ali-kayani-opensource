def phonebook(person_a: dict, person_b: dict ) -> dict:
    """
    Demonstrates the use of unpacking dicts using **
    """
    return {
        **person_a,
        **person_b
    }
