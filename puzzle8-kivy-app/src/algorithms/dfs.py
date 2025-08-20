from algorithms.utils import get_possible_moves, is_goal_state

def dfs(puzzle):
    stack = [(puzzle, [])]  # stack of (current state, path to reach it)
    visited = set()  # to keep track of visited states

    while stack:
        current, path = stack.pop()
        visited.add(current)

        if is_goal_state(current):
            return path  # return the path to the solution

        for move in get_possible_moves(current):
            if move not in visited:
                stack.append((move, path + [move]))

    return None  # return None if no solution is found