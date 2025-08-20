from typing import List, Tuple

class Puzzle:
    def __init__(self, state: Tuple[int, ...]):
        self.state = state
        self.blank_index = state.index(0)
        self.size = 3  # 3x3 puzzle

    def is_goal(self) -> bool:
        return self.state == (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def possible_moves(self) -> List[Tuple[int, ...]]:
        moves = []
        row, col = divmod(self.blank_index, self.size)

        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        for direction, (dr, dc) in directions.items():
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                new_index = new_row * self.size + new_col
                new_state = list(self.state)
                new_state[self.blank_index], new_state[new_index] = new_state[new_index], new_state[self.blank_index]
                moves.append(tuple(new_state))

        return moves

    def move(self, new_state: Tuple[int, ...]) -> None:
        self.state = new_state
        self.blank_index = new_state.index(0)

    def is_solvable(self) -> bool:
        inversions = 0
        flat_state = [num for num in self.state if num != 0]
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1
        return inversions % 2 == 0

    def __str__(self) -> str:
        return f"Current state: {self.state}"