from functions.phonebook import phonebook

# Behviours:

# 1. Merge a dictionary

def test_merge() -> None:
    """
    Tests demonstrating how to merge using **
    """    
    # given
    test_wrapper = None

    test_person_a = {
        'name': 'Homer Simpson',
        'phone': '056375863',
        'email': 'homer.s@simpsons.com'
    }
    test_person_b = {
        'name': 'Wyatt Earp',
        'phone': '896832456 ',
        'email': 'wyatt.e@outlaw.com'
    }

    # when
    test_wrapper = phonebook(test_person_a, test_person_b)
    
    # then
    assert test_wrapper == {
        **test_person_a,
        **test_person_b
    }
