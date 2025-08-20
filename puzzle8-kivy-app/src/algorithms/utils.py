from typing import List, Tuple

def manhattan(state: Tuple[int]) -> int:
    distance = 0
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)
    }
    
    for index, value in enumerate(state):
        if value != 0:  # Skip the empty tile
            goal_x, goal_y = goal_positions[value]
            current_x, current_y = divmod(index, 3)
            distance += abs(goal_x - current_x) + abs(goal_y - current_y)
    
    return distance

def misplaced(state: Tuple[int]) -> int:
    return sum(1 for index, value in enumerate(state) if value != 0 and value != index + 1)

def is_solvable(state: Tuple[int]) -> bool:
    inversions = 0
    flat_state = [value for value in state if value != 0]
    
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
    
    return inversions % 2 == 0

def get_possible_moves(state: Tuple[int]) -> List[Tuple[int]]:
    moves = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            moves.append(tuple(new_state))
    
    return moves