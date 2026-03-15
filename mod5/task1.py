class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if not self.end:
            raise IndexError('Stack is empty')
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        current = self.end
        elems = []
        while current:
            elems.append(str(current.data))
            current = current.pref
        print(' ->\n '.join(elems))
