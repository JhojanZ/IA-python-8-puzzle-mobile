from Utils.Utils import State, Problem, Node, reconstruct_path
from Data_Structure.Stack import Stack

def DFS(problem: Problem, depth_limit=None):
    frontier = Stack()
    frontier.push(Node(problem.initial_state()))
    explored = set()
    expanded = 0
    while not frontier.is_empty():
        n = frontier.pop()
        if problem.is_goal(n.state): return reconstruct_path(n), expanded
        if n.state in explored: continue
        if depth_limit is not None and n.depth > depth_limit: continue
        explored.add(n.state); expanded += 1
        for c in n.expand(problem): frontier.push(c)
    return None, expanded