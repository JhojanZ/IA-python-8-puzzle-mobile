from Utils.Puzzle8 import GOAL, GOAL_POS, PuzzleState

def misplaced(s: PuzzleState) -> int:
    return sum(1 for i,v in enumerate(s.tiles) if v != 0 and v != GOAL[i])

def manhattan(s: PuzzleState) -> int:
    dist = 0
    for i,v in enumerate(s.tiles):
        if v == 0: continue
        gi = GOAL_POS[v]
        x1,y1 = divmod(i,3); x2,y2 = divmod(gi,3)
        dist += abs(x1-x2) + abs(y1-y2)
    return dist