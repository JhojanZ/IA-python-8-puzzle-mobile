from Data_Structure.Stack import Stack
from Data_Structure.Queue import Queue
from Data_Structure.PriorityQueue import PriorityQueue
from Data_Structure.MinHeap import MinHeap

# Tests rápidos
s = Stack()
for i in range(3): s.push(i)
assert s.pop()==2 and s.pop()==1 and s.pop()==0
q = Queue()
for i in range(3): q.enqueue(i)
assert q.dequeue()==0 and q.dequeue()==1 and q.dequeue()==2
h = MinHeap()
for x in [5,1,4,2,3]: h.push(x)
assert [h.pop(), h.pop(), h.pop(), h.pop(), h.pop()] == [1,2,3,4,5]
print("Estructuras OK")