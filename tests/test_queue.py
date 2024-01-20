import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_str(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(str(queue), "data1\ndata2\ndata3")
