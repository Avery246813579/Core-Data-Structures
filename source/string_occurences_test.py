import unittest
from string_occurences import in_string, index_in_string, indexes_in_string


class TestPalindromes(unittest.TestCase):
    def test_in_string_is_in(self):
        assert in_string('abcdef', 'abc') is True
        assert in_string('abcdef', 'def') is True
        assert in_string('abcdef', 'bcde') is True
        assert in_string('ababc', 'abc') is True
        assert in_string("abcdef", 'a') is True
        assert in_string("abcdef", 'f') is True
        assert in_string("abcdef", 'c') is True

    def test_in_string_not_in(self):
        assert in_string('abcdef', 'e') is False
        assert in_string('abcdef', 'asdfaccs') is False


if __name__ == '__main__':
    unittest.main()
