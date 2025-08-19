from Data_Structure.PriorityQueue import PriorityQueue
from Utils.Utils import Problem, Node, reconstruct_path

def UCS(problem: Problem):
    pq = PriorityQueue()
    start = Node(problem.initial_state())
    pq.push(0.0, start)
    best = {start.state: 0.0}
    expanded = 0
    while not pq.is_empty():
        n = pq.pop()
        if problem.is_goal(n.state): return reconstruct_path(n), expanded
        expanded += 1
        for c in n.expand(problem):
            if c.state not in best or c.g < best[c.state]:
                best[c.state] = c.g
                pq.push(c.g, c)
    return None, expanded