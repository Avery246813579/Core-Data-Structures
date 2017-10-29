
def in_string(text, pattern):
    """ Checks if a pattern is inside a string

    :param text:        The string we want to check if a pattern is in
    :param pattern:     The pattern we want to check is in a string
    :return:            If the pattern is in the string
    """

    # return in_string_iterative(text, pattern)
    return  in_string_recursively(text, pattern)


def in_string_iterative(text, pattern):
    """ Checking if a pattern is in a string iteratively """

    text_index = 0
    pattern_index = 0

    text_length = len(text)
    pattern_length = len(pattern)

    # Loop through our text characters until we reach the end
    while text_index < text_length:
        # If our current text character is equal to our pattern character increase the index
        if text[text_index] == pattern[pattern_index]:
            pattern_index += 1
        # If our current text character is not our pattern character and if we were checking for a pattern, we want to
        # reset the pattern and try again
        elif pattern_index > 0:
            pattern_index = 0
            continue

        # If our pattern index is equal to our pattern length then we found a match and we can return True
        if pattern_index + 1 > pattern_length:
            return True

        # Go to next character
        text_index += 1

    # If we have not found our pattern then we return False
    return False


def in_string_recursively(text, pattern, text_index=0, pattern_index=0):
    """ Checking if a pattern is in a string recursively """

    # If our text index is greater then our text then the pattern was not found
    if text_index + 1 > len(text):
        return False

    # If our text character is our pattern character increase our pattern index
    if text[text_index] == pattern[pattern_index]:
        pattern_index += 1
    # If our text character is not our pattern character and our pattern_index is greater then 0 (we were checking) then
    # lets reset checking from our current index and set our pattern to it's start
    elif pattern_index > 0:
        return in_string_recursively(text, pattern, text_index, 0)

    # If our pattern index is greater then the len of the pattern then we have a match and we return true
    if pattern_index + 1 > len(pattern):
        return True

    # Go to the next character in our text string
    return in_string_recursively(text, pattern, text_index + 1, pattern_index)


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
