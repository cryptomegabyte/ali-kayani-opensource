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
        'name_a': 'Homer Simpson',
        'phone_a': '056375863',
        'email_a': 'homer.s@simpsons.com'
    }
    test_person_b = {
        'name_b': 'Wyatt Earp',
        'phone_b': '896832456 ',
        'email_b': 'wyatt.e@outlaw.com'
    }

    # when
    test_wrapper = phonebook(test_person_a, test_person_b)
    
    # then
    assert test_wrapper == {
        **test_person_a,
        **test_person_b
    }
