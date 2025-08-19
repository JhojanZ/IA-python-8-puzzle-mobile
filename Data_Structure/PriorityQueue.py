from Data_Structure.MinHeap import MinHeap

class PriorityQueue:
    # Evita comparar objetos no ordenables con un tiebreaker
    def __init__(self): self._h = MinHeap(); self._t = 0
    def push(self, priority, item):
        self._t += 1
        self._h.push((priority, self._t, item))
    def pop(self):
        return self._h.pop()[2]
    def is_empty(self): return self._h.is_empty()
    def __len__(self): return len(self._h)
