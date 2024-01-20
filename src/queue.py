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
        return f"Node({self.data})"

    def __str__(self):
        return f"{self.data}"


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.queue = []
        self.head = ""
        self.tail = None

    def __str__(self):
        text = ','.join(self.queue)
        enter_text = text.replace(',', '\n')

        return f"{enter_text}"

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if len(self.queue) == 0:
            self.head = new_node
            self.tail = new_node
            self.queue.append(data)
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.queue.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass
