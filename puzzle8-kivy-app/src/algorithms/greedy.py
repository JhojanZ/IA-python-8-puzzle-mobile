from IA.No_Informada.Heuristicas.Heuristicas import manhattan

def greedy(puzzle):
    # Implement the Greedy Best-First Search algorithm
    # Initialize the open list with the starting state
    open_list = [puzzle]
    closed_list = set()

    while open_list:
        # Sort the open list based on the heuristic (Manhattan distance)
        open_list.sort(key=lambda x: manhattan(x))
        current = open_list.pop(0)  # Get the state with the lowest heuristic value

        if current.is_goal():
            return current.get_solution_steps()  # Return the solution steps

        closed_list.add(current)

        for neighbor in current.get_neighbors():
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)

    return None  # Return None if no solution is found