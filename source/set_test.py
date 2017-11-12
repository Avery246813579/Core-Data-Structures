from set import Set
import unittest


class BinaryTreeNodeTest(unittest.TestCase):
    def test_init(self):
        test_set = Set([1, 2, 3, 4])
        assert test_set.size == 4

    def test_add(self):
        test_set = Set()
        assert test_set.size == 0
        test_set.add(1)
        assert test_set.size == 1
        test_set.add(2)
        assert test_set.size == 2
        test_set.add(2)
        assert test_set.size == 2

    def test_remove(self):
        test_set = Set([1, 2, 3, 4])
        assert test_set.size == 4
        test_set.remove(3)
        assert test_set.size == 3
        with self.assertRaises(KeyError):
            test_set.remove(3)
        test_set.remove(2)
        assert test_set.size == 2

    def test_contains(self):
        test_set = Set([1, 2, 3, 4])
        assert test_set.contains(2) is True
        test_set.remove(2)
        assert test_set.contains(2) is False

    def test_union(self):
        first_set = Set([1, 2, 3, 4])
        second_set = Set([3, 4, 5, 6])

        assert first_set.union(second_set).size == 6

    def test_intersection(self):
        first_set = Set([1, 2, 3, 4])
        second_set = Set([3, 4, 5, 6])

        assert first_set.intersection(second_set).size == 2

    def test_difference(self):
        first_set = Set([1, 2, 3, 4, 9])
        second_set = Set([3, 4, 9, 5, 6, 7])

        assert first_set.difference(second_set).size == 2

    def test_subset(self):
        test_set = Set([1, 2, 3, 4, 5])

        assert test_set.is_subset(Set([2, 3, 4])) is True
        assert test_set.is_subset(Set([2, 6, 7, 8])) is False


if __name__ == '__main__':
    unittest.main()
