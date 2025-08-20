from run import select_algorithm, Algorithm
from app import Puzzle8App

def main():
    print("Puzzle-8 AI Solver Initialized.")
    select_algorithm(Algorithm.BFS)
    select_algorithm(Algorithm.DFS)
    select_algorithm(Algorithm.UCS)
    select_algorithm(Algorithm.GREEDY_MANHATTAN)
    select_algorithm(Algorithm.GREEDY_MISPLACED)
    select_algorithm(Algorithm.ASTAR_MANHATTAN)
    select_algorithm(Algorithm.ASTAR_MISPLACED)

if __name__ == "__main__":
    Puzzle8App().run()
