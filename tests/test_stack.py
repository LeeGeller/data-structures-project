"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_node(self):
        node_1 = Node('a', 2)

        self.assertEqual(Node(5, None).data, 5)
        self.assertEqual(Node(5, node_1).next_node, node_1)

    def test_stack(self):
        stack = Stack()
        stack.push('data')

        self.assertEqual(stack.top.data, 'data')

        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data')

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data')
        stack.push('data2')

        deleted_data = stack.pop()

        self.assertEqual(deleted_data, 'data2')
        self.assertEqual(stack.top.data, 'data')
        self.assertEqual(len(stack.stack), 1)

