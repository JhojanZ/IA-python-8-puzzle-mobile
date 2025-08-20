# Puzzle-8 Kivy Application

This project is a Kivy-based mobile application designed to visualize various algorithms for solving the 8-puzzle problem. The application allows users to select different algorithms and see how they solve the puzzle step by step.

## Project Structure

```
puzzle8-kivy-app
├── src
│   ├── main.py                # Entry point of the Kivy application
│   ├── ui
│   │   ├── screens.py         # Defines the screens of the application
│   │   └── widgets.py         # Contains custom Kivy widgets
│   ├── algorithms
│   │   ├── bfs.py             # Implements Breadth-First Search algorithm
│   │   ├── dfs.py             # Implements Depth-First Search algorithm
│   │   ├── ucs.py             # Implements Uniform Cost Search algorithm
│   │   ├── greedy.py          # Implements Greedy Best-First Search algorithm
│   │   ├── astar.py           # Implements A* algorithm
│   │   └── utils.py           # Utility functions and constants
│   ├── models
│   │   └── puzzle.py          # Represents the state of the 8-puzzle
│   └── assets
│       └── styles.kv          # Kivy language definitions for UI layout
├── requirements.txt            # Lists project dependencies
├── README.md                   # Documentation for the project
└── .gitignore                  # Specifies files to ignore by Git
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd puzzle8-kivy-app
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the main script to start the application:
   ```
   python src/main.py
   ```

## Usage

- Upon launching the application, users will be presented with a main menu.
- Users can select an algorithm from the menu to visualize how it solves the 8-puzzle.
- The application will display the steps taken by the selected algorithm to reach the goal state.

## Overview of Algorithms

- **Breadth-First Search (BFS)**: Explores all possible states at the present depth prior to moving on to the nodes at the next depth level.
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
- **Uniform Cost Search (UCS)**: Expands the least costly node first, ensuring the optimal solution.
- **Greedy Best-First Search**: Uses a heuristic to estimate the cost from the current node to the goal, expanding the most promising node.
- **A***: Combines features of UCS and Greedy, using both the cost to reach the node and the estimated cost to reach the goal.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.