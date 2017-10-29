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
        assert in_string('abcdef', 'k') is False
        assert in_string('abcdef', 'asdfaccs') is False

    def test_index_in_string_is_in(self):
        assert index_in_string('abcdef', 'abc') == 0
        assert index_in_string('abcdef', 'def') == 3
        assert index_in_string('abcdef', 'bcde') == 1
        assert index_in_string('ababc', 'abc') == 2
        assert index_in_string("abcdef", 'a') == 0
        assert index_in_string("abcdef", 'f') == 5
        assert index_in_string("abcdef", 'c') == 2

    def test_in_string_not_in(self):
        assert index_in_string('abcdef', 'k') == -1
        assert index_in_string('abcdef', 'asdfaccs') == -1

    def test_indexes_in_string(self):
        assert indexes_in_string('ababab', 'ab') == [0, 2, 4]
        assert indexes_in_string('abcdeabcde', 'abc') == [0, 5]
        assert indexes_in_string('abababcd', 'aba') == [0, 2]
        assert indexes_in_string('i123mydog', '123') == [1]

    def test_indexes_in_string_not_in(self):
        assert indexes_in_string('ababab', 'ds') == []
        assert indexes_in_string('abcdeabcde', 'dead') == []

if __name__ == '__main__':
    unittest.main()
