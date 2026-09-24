class Stack:
    """
    Стек (LIFO) на базе динамического массива (list).
    Все операции — O(1) амортизированно.
    """
    def __init__(self):
        self._data = []

    def push(self, item):
        """Кладём элемент на вершину. O(1) амортизированно."""
        self._data.append(item)

    def pop(self):
        """Снимаем элемент с вершины. O(1)."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._data.pop()

    def peek(self):
        """Смотрим вершину без снятия. O(1)."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        # итерируемся от вершины к основанию
        return reversed(self._data)

    def __repr__(self):
        return f"Stack({self._data})"
