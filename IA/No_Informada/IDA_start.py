from Utils.Puzzle8 import Problem
from Utils.Utils import Node, reconstruct_path
from Data_Structure.PriorityQueue import PriorityQueue

def IDA_star(problem: Problem, h):
    from math import inf
    start = Node(problem.initial_state())
    bound = h(start.state)
    expanded_total = 0

    def dfs_limited(n, g, bound):
        nonlocal expanded_total
        f = g + h(n.state)
        if f > bound: return f, None
        if problem.is_goal(n.state): return f, reconstruct_path(n)
        m = inf
        for c in n.expand(problem):
            expanded_total += 1
            t, sol = dfs_limited(c, g + (c.g - n.g), bound)
            if sol is not None: return t, sol
            if t < m: m = t
        return m, None

    while True:
        t, sol = dfs_limited(start, 0, bound)
        if sol is not None: return sol, expanded_total
        if t == float("inf"): return None, expanded_total
        bound = t