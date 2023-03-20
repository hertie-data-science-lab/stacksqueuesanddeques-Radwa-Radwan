class ArrayDeque:
    DEFAULT_CAPACITY = 80

    def __init__(self):
        self.elements = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self.front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.elements[self.front]

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        back = (self.front + self._size - 1) % len(self.elements)
        return self.elements[back]

    def add_first(self, e):
        if self._size == len(self.elements):
            self._resize(2 * len(self.elements))
        self.front = (self.front - 1) % len(self.elements)
        self.elements[self.front] = e
        self._size += 1

    def add_last(self, e):
        if self._size == len(self.elements):
            self._resize(2 * len(self.elements))
        back = (self.front + self._size) % len(self.elements)
        self.elements[back] = e
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self.elements[self.front]
        self.elements[self.front] = None
        self.front = (self.front + 1) % len(self.elements)
        self._size -= 1
        return answer

    def _resize(self, cap):
        old = self.elements
        self.elements = [None] * cap
        walk = self.front
        for k in range(self._size):
            self.elements[k] = old[walk]
            walk = (walk + 1) % len(old)
        self.front = 0