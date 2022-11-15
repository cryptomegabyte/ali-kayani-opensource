from app.binary_search import binary_search

"""
Tests for binary search function

Behaviours:

1. Should return index of search item.
"""

def test_binary_search() -> None:
    # given
    test_wrapper = None

    # when
    test_wrapper = binary_search([4,6,9,13,18,18])

    # then
    assert test_wrapper == 1