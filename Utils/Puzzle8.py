from Utils.Utils import State, Problem 

# Representación: tupla de 9 ints; 0 = hueco
GOAL = (1,2,3,4,5,6,7,8,0)
GOAL_POS = {v:i for i,v in enumerate(GOAL)}

class PuzzleState(State):
    __slots__ = ("tiles",)
    def __init__(self, tiles): self.tiles = tuple(tiles)
    def key(self): return self.tiles
    def __repr__(self): return f"PuzzleState{self.tiles}"

class Puzzle(Problem):
    def __init__(self, start):
        self.start = PuzzleState(start)
    def initial_state(self) -> State: return self.start
    def is_goal(self, s: PuzzleState) -> bool: return s.tiles == GOAL
    def actions(self, s: PuzzleState):
        i = s.tiles.index(0); x,y = divmod(i,3)
        for dx,dy,a in ((1,0,"DOWN"),(-1,0,"UP"),(0,1,"RIGHT"),(0,-1,"LEFT")):
            nx,ny = x+dx,y+dy
            if 0 <= nx < 3 and 0 <= ny < 3: yield a
    def result(self, s: PuzzleState, a):
        delta = {"DOWN":(1,0),"UP":(-1,0),"RIGHT":(0,1),"LEFT":(0,-1)}[a]
        i = s.tiles.index(0); x,y = divmod(i,3)
        nx,ny = x+delta[0], y+delta[1]; j = nx*3+ny
        tiles = list(s.tiles); tiles[i], tiles[j] = tiles[j], tiles[i]
        return PuzzleState(tiles)
    
    def is_solvable(self):
        # Contar las inversiones

        return self.inversion() % 2 == 0

    def inversion(self):
        inversions = 0
        flat_tiles = [tile for tile in self.start.tiles if tile != 0]
        for i in range(len(flat_tiles)):
            for j in range(i + 1, len(flat_tiles)):
                if flat_tiles[i] > flat_tiles[j]:
                    inversions += 1
        # Un puzzle es solucionable si el número de inversiones es par
        return inversions
        
