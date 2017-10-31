#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)

    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)
    # return is_palindrome_dumb(text)


IGNORE_CHARACTERS = [' ', ',', '.', '!', '?', '\'', '-']


def is_palindrome_dumb(text):
    text = text.lower().replace(' ', '').replace(',', '').replace('.', '').replace('!', '').replace('?', '',).replace('\'', '').replace('-', '')
    return text == text[::-1]


def is_palindrome_iterative(text):
    """

    BEST: O(nm) or (n / 2) * m
    WORST: O(nm)  or (n / 2) * 2m
    """
    left_index = 0
    right_index = len(text) - 1

    # We keep looping until the characters meet or overlap
    while right_index > left_index:  # n (number of characters) / 2 or O(n)
        # If it's an ignored character go to the next loop
        if text[left_index] in IGNORE_CHARACTERS:  # m (number of IGNORED_CHARACTERS)
            left_index += 1
            continue

        # If it's an ignored character go to the next loop
        if text[right_index] in IGNORE_CHARACTERS:  # m (number of IGNORED_CHARACTERS)
            right_index -= 1
            continue

        # If the two sides don't match then it's not a palindrome
        if text[left_index].lower() != text[right_index].lower():
            return False

        # Increase to do our next step
        left_index += 1
        right_index -= 1

    # If we go through the loop with no returns then it's a palindrome
    return True


def is_palindrome_recursive(text, left_index=0, right_index=None):
    """

    BEST: O(nm) or (n / 2) * m
    WORST: O(nm)  or (n / 2) * 2m
    """

    # If our right character is undefined
    if right_index is None:
        right_index = len(text) - 1

    # If we overlap characters then return back
    if right_index - 1 < left_index:  # right - 1 < left is equal to right <= left
        return True

    # If our left character is a character we want to ignore, then go to the next character.
    if text[left_index] in IGNORE_CHARACTERS:
        return is_palindrome_recursive(text, left_index + 1, right_index)

    # If our right character is a character we want to ignore, then go to the next character.
    if text[right_index] in IGNORE_CHARACTERS:
        return is_palindrome_recursive(text, left_index, right_index - 1)

    # If our left and right characters are the same then keep looking
    if text[left_index].lower() == text[right_index].lower():
        return is_palindrome_recursive(text, left_index + 1, right_index - 1)

    # If our characters are not the same return false
    return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
