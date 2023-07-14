""" This module was created for the sake of being imported. """

print("Imported test_module...")

test_string = "Greetings friend!"


def find_index(
    to_search, target
):  # Takes in a 'list' to search; and a target value users wish to find.
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1  # In cases where user function does not find index value; returns '-1'.
