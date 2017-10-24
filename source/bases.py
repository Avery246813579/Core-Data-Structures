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
        base10 += _get_ascii_index(digits[i]) * math.pow(base, len(digits) - i - 1)

    return base10


dal = string.digits + string.ascii_lowercase
dau = string.digits + string.ascii_uppercase
dalu = string.digits + string.ascii_letters


def _get_ascii_index(digit):
    for i in range(len(dalu)):
        if digit == dalu[i]:
            if i > 35:
                return i - 26

            return i


def encode(number, base, uppercase=False):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    i = 0
    max_value = 0
    final = ''

    while max_value < number:
        max_value = math.pow(base, i)

        i += 1

    i -= 2

    for i in range(i, -1, -1):
        power = math.pow(base, i)
        if number - power > -1:
            left_over = int(power % number)

            if left_over < 1:
                taking = int(number)
            else:
                taking = int(number / left_over)

            number -= taking * power
            final += dal[taking]
        else:
            final += '0'

    if number > 0:
        return str(number)

    return final


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    return


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
    # main()
    ...
