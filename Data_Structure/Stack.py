class Stack:
    def __init__(self): self._a = []
    def push(self, x): self._a.append(x)
    def pop(self):
        if not self._a: raise IndexError("pop from empty Stack")
        return self._a.pop()
    def is_empty(self): return not self._a
    def __len__(self): return len(self._a)