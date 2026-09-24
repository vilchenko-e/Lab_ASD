class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        """Кладём элемент на вершину."""
        self._data.append(item)

    def pop(self):
        """Снимаем элемент с вершины."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._data.pop()

    def peek(self):
        """Смотрим вершину без снятия."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"
