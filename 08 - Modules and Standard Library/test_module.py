print("Imported test_module...")

test_string = "Greetings friend!"


def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
