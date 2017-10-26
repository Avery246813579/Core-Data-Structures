#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
import math


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    base10 = 0
    for i in range(len(digits)):
        base10 += string.printable.index(digits[i].lower()) * math.pow(base, len(digits) - i - 1)

    return int(base10)


def encode(number, base):
    """ Encode given number in base 10 to digits in given base.

        average: O(n) or 2n
        best: O(n) or n

        number: int -- integer representation of number (in base 10)
        base: int -- base to convert to
        return: str -- string representation of number (in given base)
    """

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    max_value = 0
    digit_index = 0

    while max_value <= number:
        max_value = math.pow(base, digit_index)

        digit_index += 1

    # Remove the digit we just added before the check and subtract another because we checked against the max
    digit_index -= 2

    encoded_solution = ''
    for i in range(digit_index, -1, -1):
        # If the rest of the digits are 0, let's just add those then return our solution
        if number == 0:
            encoded_solution += '0' * (i + 1)

            return encoded_solution

        # The power of the index. Like b^i
        power = math.pow(base, i)

        # If our number is greater then the value power at the current index, then we want to continue by getting the
        # character we need and adding it. If our current number is lower then we add a 0.
        if number - power > -1:
            left_over = int(power % number)

            if left_over < 1:
                division_times = 1
            else:
                division_times = int(number / power)

            # Remove the number we are taking away
            number -= division_times * power

            # We can use division times to get the digit we want
            encoded_solution += string.printable[division_times]
        else:
            encoded_solution += '0'

    return encoded_solution


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # This is bad
    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
