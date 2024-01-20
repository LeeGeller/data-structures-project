from queue import Queue as q


class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node({self.data}, {self.next_node})"

    def __str__(self):
        return f"{self.data}"


class Queue(q):
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.queue = []
        self.head = ""
        self.tail = None

    def __str__(self):
        return f"{self.head}"

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        new_node.next_node = self.tail
        q.put(self.queue, new_node.data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass


n = Node(5)
qu = Queue()
qu.enqueue(n)

print(qu.queue)
