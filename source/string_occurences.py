
def in_string(text, pattern):
    """ Checks if a pattern is inside a string

    :param text:        The string we want to check if a pattern is in
    :param pattern:     The pattern we want to check is in a string
    :return:            If the pattern is in the string
    """

    return in_string_iterative(text, pattern)
    # return  in_string_recursively(text, pattern)


def in_string_iterative(text, pattern):
    """ Checking if a pattern is in a string iteratively """

    text_index = 0
    pattern_index = 0

    text_length = len(text)
    pattern_length = len(pattern)

    while text_index < text_length:
        if text[text_index] == pattern[pattern_index]:
            pattern_index += 1
        elif pattern_index > 0:
            pattern_index = 0
            continue

        if pattern_index + 1 > pattern_length:
            return True

        text_index += 1

    return False

def in_string_recursively(text, pattern, text_index=0, pattern_index=0):
    """ Checking if a pattern is in a string recursively """

    pass


def index_in_string(text, pattern):
    """ Returns the index the pattern starts of a given string. Or returns -1 if it doesn't show up

    :param text:        The string we want to check
    :param pattern:     The pattern we want to check
    """

    return index_in_string_iterative(text, pattern)
    # return index_in_string_recursive(text, pattern)



def index_in_string_iterative(text, pattern):
    pass


def index_in_string_recursive(text, pattern, text_index=0, pattern_index=0):
    pass


def indexes_in_string(text, pattern):
    """ Returns all the indexes of a pattern in a given string. Or returns None if None show up

    :param text:        The string we want to check
    :param pattern:     The pattern we want to check
    """

    return indexes_in_string_iterative(text, pattern)
    # return indexes_in_string_iterative(text, pattern)


def indexes_in_string_iterative(text, pattern):
    pass


def index_in_string_recursive(text, pattern, text_index=0, pattern_index=0):
    pass
