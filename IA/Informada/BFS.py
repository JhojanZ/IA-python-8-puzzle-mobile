from Data_Structure.Queue import Queue
from Utils.Utils import Problem, Node, reconstruct_path

def BFS(problem: Problem):
    frontier = Queue()
    frontier.enqueue(Node(problem.initial_state()))
    explored = set()
    expanded = 0
    while not frontier.is_empty():
        n = frontier.dequeue()
        if problem.is_goal(n.state): return reconstruct_path(n), expanded
        if n.state in explored: continue
        explored.add(n.state); expanded += 1
        for c in n.expand(problem): frontier.enqueue(c)
    return None, expanded
