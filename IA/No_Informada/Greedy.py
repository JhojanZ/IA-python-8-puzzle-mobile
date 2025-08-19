from Utils.Puzzle8 import Problem
from Utils.Utils import Node, reconstruct_path
from Data_Structure.PriorityQueue import PriorityQueue

def Greedy(problem: Problem, h):
    pq = PriorityQueue()
    start = Node(problem.initial_state())
    pq.push(h(start.state), start)
    seen = set()
    expanded = 0
    while not pq.is_empty():
        n = pq.pop()
        if problem.is_goal(n.state): return reconstruct_path(n), expanded
        if n.state in seen: continue
        seen.add(n.state); expanded += 1
        for c in n.expand(problem): pq.push(h(c.state), c)
    return None, expanded