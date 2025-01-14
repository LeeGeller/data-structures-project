import unittest

from src.queue import Queue, Node


class TestQueue(unittest.TestCase):

    def test_str_queue(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(str(queue), "data1\ndata2\ndata3")

    def test_str_node(self):
        node = Node('data1')

        self.assertEqual(str(node), "data1")

    def test_enqueue(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.head.next_node.next_node.data, 'data3')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.next_node, None)

    def test_dequeue(self):
        queue = Queue()

        queue.enqueue('data1')

        self.assertEqual(queue.dequeue(), 'data1')

        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue(None)
        self.assertEqual(queue.dequeue(), None)

    def test_dequeue_len(self):
        queue = Queue()

        self.assertEqual(len(queue.queue), 0)
        self.assertEqual(len(queue.head), 0)

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(len(queue.queue), 3)

        queue.dequeue()

        self.assertEqual(len(queue.queue), 2)

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(len(queue.queue), 0)
