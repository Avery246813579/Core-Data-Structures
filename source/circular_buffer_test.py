from circular_buffer import CircularBuffer
import unittest


class NodeTest(unittest.TestCase):
    def test_insert(self):
        buffer = CircularBuffer(2)
        buffer.insert(0)
        assert buffer.values() == [0, None]
        buffer.insert(1)
        assert buffer.values() == [0, 1]
        buffer.insert(2)
        assert buffer.values() == [2, 1]
