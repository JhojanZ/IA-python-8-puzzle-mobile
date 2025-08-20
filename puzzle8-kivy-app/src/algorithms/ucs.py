from models.puzzle import Puzzle
import heapq

def ucs(start_state):
    start_puzzle = Puzzle(start_state)
    if not start_puzzle.is_solvable():
        return None

    frontier = []
    heapq.heappush(frontier, (0, start_puzzle))
    explored = set()
    came_from = {}
    cost_so_far = {start_puzzle: 0}

    while frontier:
        current_cost, current_puzzle = heapq.heappop(frontier)

        if current_puzzle.is_goal():
            return reconstruct_path(came_from, current_puzzle)

        explored.add(current_puzzle)

        for next_puzzle in current_puzzle.get_neighbors():
            new_cost = cost_so_far[current_puzzle] + 1  # Assuming each move has a cost of 1
            if next_puzzle not in cost_so_far or new_cost < cost_so_far[next_puzzle]:
                cost_so_far[next_puzzle] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, next_puzzle))
                came_from[next_puzzle] = current_puzzle

    return None

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path