class MinHeap:
    # Montículo mínimo binario 1-indexed
    def __init__(self): self._a = [None]
    def __len__(self): return len(self._a)-1
    def is_empty(self): return len(self) == 0
    def push(self, x):
        self._a.append(x); self._sift_up(len(self))
    def pop(self):
        if self.is_empty(): raise IndexError("pop from empty heap")
        root = self._a[1]; last = self._a.pop()
        if not self.is_empty():
            self._a[1] = last; self._sift_down(1)
        return root
    def _sift_up(self, i):
        while i > 1:
            p = i//2
            if self._a[p] <= self._a[i]: break
            self._a[p], self._a[i] = self._a[i], self._a[p]; i = p
    def _sift_down(self, i):
        n = len(self)
        while 2*i <= n:
            l, r = 2*i, 2*i+1
            m = l if r > n or self._a[l] <= self._a[r] else r
            if self._a[i] <= self._a[m]: break
            self._a[i], self._a[m] = self._a[m], self._a[i]; i = m
