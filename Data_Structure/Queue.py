class Queue:
    # Cola circular para O(1) amortizado
    def __init__(self, capacity=16):
        self._a = [None]*capacity; self._head = 0; self._tail = 0; self._size = 0
    def _grow(self):
        b = [None]*(len(self._a)*2)
        for i in range(self._size):
            b[i] = self._a[(self._head+i) % len(self._a)]
        self._a, self._head, self._tail = b, 0, self._size
    def enqueue(self, x):
        if self._size == len(self._a): self._grow()
        self._a[self._tail] = x
        self._tail = (self._tail+1) % len(self._a)
        self._size += 1
    def dequeue(self):
        if self._size == 0: raise IndexError("dequeue from empty Queue")
        x = self._a[self._head]; self._a[self._head] = None
        self._head = (self._head+1) % len(self._a)
        self._size -= 1
        return x
    def is_empty(self): return self._size == 0
    def __len__(self): return self._size