from IA.No_Informada.A_start import A_star
from .utils import manhattan

def astar_algorithm(puzzle_state):
    # Create an instance of the puzzle with the given state
    puzzle = Puzzle(puzzle_state)
    
    # Run the A* algorithm using the Manhattan heuristic
    solution = A_star(puzzle, manhattan)
    
    return solution