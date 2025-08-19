from Utils.Puzzle8 import Puzzle, GOAL, GOAL_POS

from IA.Informada.BFS import BFS
from IA.Informada.DFS import DFS
from IA.Informada.UCS import UCS

from IA.No_Informada.Heuristicas.Heuristicas import misplaced, manhattan
from IA.No_Informada.Greedy import Greedy
from IA.No_Informada.A_start import A_star
from IA.No_Informada.IDA_start import IDA_star



import time

def run_and_measure(problem, algorithms):
    rows = []
    for name, fn in algorithms:
        t0 = time.time()
        result, expanded = fn(problem)
        dt = time.time() - t0
        if result is None:
            depth = None; cost = None; steps = None
        else:
            steps = [a for a,_ in result][1:]  # acciones excluyendo el None inicial
            depth = len(steps)
            cost = result[-1][1]  # estado final (no usamos g aquí por simplicidad)
        rows.append((name, expanded, depth, dt))
        print(f"{name:18s} | expandidos={expanded:6} | profundidad={depth} | tiempo={dt:.3f}s")
    return rows

# Instancia de prueba
START = (1,4,2,7,5,3,0,8,6)  # puedes cambiarla por otras
p = Puzzle(START)

"""
algos = [
    ("BFS", lambda pr: BFS(pr)),
    ("DFS", lambda pr: DFS(pr)),
    ("UCS", lambda pr: UCS(pr)),
    ("Greedy(manhattan)", lambda pr: Greedy(pr, manhattan)),
    ("A*(manhattan)", lambda pr: A_star(pr, manhattan)),
    ("A*(misplaced)", lambda pr: A_star(pr, misplaced)),
    ("IDA*(manhattan)", lambda pr: IDA_star(pr, manhattan)),
]
"""
algos = [
    ("BFS", lambda pr: BFS(pr)),
    ("DFS", lambda pr: DFS(pr)),
    ("UCS", lambda pr: UCS(pr)),
    ("Greedy(manhattan)", lambda pr: Greedy(pr, manhattan)),
    ("A*(manhattan)", lambda pr: A_star(pr, manhattan)),
    ("A*(misplaced)", lambda pr: A_star(pr, misplaced))
]
rows = run_and_measure(p, algos)
for r in rows:
    print(f"{r[0]:18s} | expandidos={r[1]:6} | profundidad={r[2]} | tiempo={r[3]:.3f}s")


"""
# Ejecuta este bloque después de correr la celda anterior para ver un gráfico de tiempos.
import matplotlib.pyplot as plt

names = [r[0] for r in rows]
times = [r[3] for r in rows]

plt.figure()
plt.bar(range(len(times)), times)
plt.xticks(range(len(times)), names, rotation=45, ha='right')
plt.ylabel('Tiempo (s)')
plt.title('Comparación de tiempos por algoritmo')
plt.tight_layout()
plt.show()
"""