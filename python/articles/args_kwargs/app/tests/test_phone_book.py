import pytest
from src.phone_book import phone_book

"""
As a software engineer I need to write a function
Which returns a dict consisting of a persons name and phone number.

"""

test_phone_book_data = [
    {
        "name": "John Doe",
        "phone_number": "00000000",
        "address": "Test address"
    },
    {
        "name": "John Doe's Wife",
        "phone_number": "00000001",
        "address": "Test address",
        "email": "test@test.com"
    },
]

@pytest.mark.parametrize("test_person,phone_record",[(test_phone_book_data[0],test_phone_book_data[0]),(test_phone_book_data[1],test_phone_book_data[1])])
def test_phone_book(test_person: dict, phone_record: dict) -> None:

    # given
    test_wrapper = None
    
    # when
    test_wrapper = phone_book(**test_person)

    # then
    assert test_wrapper == phone_record
