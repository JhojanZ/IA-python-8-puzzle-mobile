from Utils.Puzzle8 import Problem
from Utils.Utils import Node, reconstruct_path
from Data_Structure.PriorityQueue import PriorityQueue

def A_star(problem: Problem, h):
    pq = PriorityQueue()
    start = Node(problem.initial_state())
    pq.push(h(start.state) + start.g, start)
    best = {start.state: 0.0}
    expanded = 0
    while not pq.is_empty():
        n = pq.pop()
        if problem.is_goal(n.state): return reconstruct_path(n), expanded
        expanded += 1
        for c in n.expand(problem):
            f = c.g + h(c.state)
            if c.state not in best or c.g < best[c.state]:
                best[c.state] = c.g
                pq.push(f, c)
    return None, expanded