class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # начало очереди
        self.end = None    # конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if not self.start:
            raise IndexError('Queue is empty')
        val = self.start.data
        self.start = self.start.nref
        if self.start:
            self.start.pref = None
        else:
            self.end = None
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        if not self.end:
            self.start = self.end = new_node
            return 
        self.end.nref = new_node
        new_node.pref = self.end
        self.end = new_node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            if self.start:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return

        current = self.start
        i = 0
        while current and i < n:
            current = current.nref
            i += 1

        if current is None:
            raise IndexError('Queue index out of range')
        else:
            new_node = Node(val)
            prev_node = current.pref
            new_node.pref = prev_node
            new_node.nref = current
            current.pref = new_node
            if prev_node:
                prev_node.nref = new_node
            else:
                self.start = new_node

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current = self.start
        elems = []
        while current:
            elems.append(str(current.data))
            current = current.nref
        print(" ->\n ".join(elems))