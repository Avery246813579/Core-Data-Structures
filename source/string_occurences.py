
def in_string(text, pattern):
    """ Checks if a pattern is inside a string

    :param text:        The string we want to check if a pattern is in
    :param pattern:     The pattern we want to check is in a string
    :return:            If the pattern is in the string
    """

    # return in_string_iterative(text, pattern)
    return in_string_recursively(text, pattern)


def in_string_iterative(text, pattern):
    """ Checking if a pattern is in a string iteratively

    BEST: O(1)
    WORST: O(n)
    """

    text_index = 0
    pattern_index = 0

    text_length = len(text)
    pattern_length = len(pattern)

    # Loop through our text characters until we reach the end
    while text_index < text_length:  # O(N)
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
    """ Checking if a pattern is in a string recursively

    BEST: O(1)
    WORST: O(n)
    """

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
    return in_string_recursively(text, pattern, text_index + 1, pattern_index)  # O(n)


def index_in_string(text, pattern):
    """ Returns the index the pattern starts of a given string. Or returns -1 if it doesn't show up

    :param text:        The string we want to check
    :param pattern:     The pattern we want to check
    """

    # return index_in_string_iterative(text, pattern)
    return index_in_string_recursive(text, pattern)


def index_in_string_iterative(text, pattern):
    """ Gets the index of a pattern in a string iteratively

    BEST: O(1)
    WORST: O(n)
    """

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

        # If our pattern index is equal to our pattern length then we found a match and we can return our current text
        # index minus our patten length - 1
        if pattern_index + 1 > pattern_length:
            return text_index - (pattern_length - 1)

        # Go to next character
        text_index += 1

    # If we have not found our pattern then we return -1
    return -1


def index_in_string_recursive(text, pattern, text_index=0, pattern_index=0):
    """ Gets the index of a pattern in a string recursively

    BEST: O(1)
    WORST: O(n)
    """

    # If our text index is greater then our text then the pattern was not found and we return back -1
    if text_index + 1 > len(text):
        return -1

    # If our text character is our pattern character increase our pattern index
    # Check if the current letters match, if so check more of the pattern
    if text[text_index] == pattern[pattern_index]:
        pattern_index += 1
    # If our text character is not our pattern character and our pattern_index is greater then 0 (we were checking) then
    # lets reset checking from our current index and set our pattern to it's start
    elif pattern_index > 0:
        return index_in_string_recursive(text, pattern, text_index, 0)

    # If our pattern index is greater then the len of the pattern
    # then we have a match and we return our text index
    # minus our (pattern length - 1)
    # Check if we've looked at the whole pattern
    # If so, calculate the starting index of the match (walk back the len of pattern - 1)
    if pattern_index + 1 > len(pattern):
        return text_index - (len(pattern) - 1)

    # Go to the next character in our text string
    return index_in_string_recursive(text, pattern, text_index + 1, pattern_index)


def indexes_in_string(text, pattern):
    """ Returns all the indexes of a pattern in a given string. Or returns None if None show up

    :param text:        The string we want to check
    :param pattern:     The pattern we want to check
    """

    # return indexes_in_string_iterative(text, pattern)
    return indexes_in_string_recursive(text, pattern)


def indexes_in_string_iterative(text, pattern):
    """ Gets our indexes of a pattern from a string iteratively

    AVERAGE: O(N)
    """

    text_index = 0
    pattern_index = 0

    text_length = len(text)
    pattern_length = len(pattern)

    indexes = []

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

        # If our pattern index is equal to our pattern length then we found a match and we want to add the index of the
        # pattern start to our indexes and reset our pattern index and keep checking
        if pattern_index + 1 > pattern_length:
            indexes.append(text_index - (pattern_length - 1))
            pattern_index = 0
            continue

        # Go to next character
        text_index += 1

    # Lets return our indexes
    return indexes


def indexes_in_string_recursive(text, pattern, text_index=0, pattern_index=0):
    """ Finds all the indexes of a pattern in a text using recursion

     AVERAGE: O(n)
     """

    # If our text index is greater then our text then the pattern was not found and we return an empty array to append
    # too
    if text_index + 1 > len(text):
        return []

    # If our text character is our pattern character increase our pattern index
    if text[text_index] == pattern[pattern_index]:
        pattern_index += 1
    # If our text character is not our pattern character and our pattern_index is greater then 0 (we were checking) then
    # lets reset checking from our current index and set our pattern to it's start
    elif pattern_index > 0:
        return indexes_in_string_recursive(text, pattern, text_index, 0)

    # If our pattern index is greater then the len of the pattern then we have a match and we return our text index
    # minus our (pattern length - 1) in an array plus our already created array
    if pattern_index + 1 > len(pattern):
        return [text_index - (len(pattern) - 1)] + indexes_in_string_recursive(text, pattern, text_index, 0)

    # Go to the next character in our text string
    return indexes_in_string_recursive(text, pattern, text_index + 1, pattern_index)


def in_string_used(text, pattern):
    """ Finds if a pattern is in a string using a function made before

    BEST: O(1)
    WORST: O(n)
    """

    return index_in_string(text, pattern) != -1


def index_in_string_used(text, pattern):
    """ Finds index of the pattern in a string

    Less efficient then using own code

    AVERAGE: O(n)
    """

    indexes = indexes_in_string(text, pattern)

    if len(indexes) == 0:
        return -1

    return indexes[0]


if __name__ == '__main__':
    N = int(input())

    lst = []
    for i in range(N):
        command = input()
        split = command.split()

        if split[0] == "insert":
            lst.insert(int(split[1]), int(split[2]))
        elif split[0] == "remove":
            lst.remove(int(split[1]))
        elif split[0] == "print":
            print(lst)
        elif split[0] == "append":
            lst.insert(0, int(split[1]))
        elif split[0] == "split":
            lst.sort()
        elif split[0] == "pop":
            del lst[len(lst) - 1]
        elif split[0] == "reverse":
            lst.reverse()

