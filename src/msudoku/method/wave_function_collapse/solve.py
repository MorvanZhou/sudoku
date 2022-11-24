import typing as tp
import random

from msudoku.method.types import ListGrid
from msudoku.method.wave_function_collapse.grid import Grid
from msudoku.method.wave_function_collapse.pq import PriorityQueue
from msudoku.method.wave_function_collapse.generate import wave_function_collapse, propagate
from msudoku import checker


def solve(grid: ListGrid, max_try: int = 10) -> tp.Tuple[bool, ListGrid]:
    g, pq = reset(grid)
    attempt = 1
    while True:
        result = g.to_number()
        ok, _ = checker.check(result)
        if not ok:
            if attempt >= max_try:
                return False, g.to_number()
            g, pq = reset(grid)
            attempt += 1
        done = wave_function_collapse(g, pq)
        if done:
            break
    return True, g.to_number()


def reset(grid: ListGrid) -> tp.Tuple[Grid, PriorityQueue]:
    g = Grid()
    pq = PriorityQueue()
    rows = list(range(g.height))
    cols = list(range(g.width))
    random.shuffle(rows)
    random.shuffle(cols)
    for r in rows:
        for c in cols:
            pq.put((r, c), g.max_number)

    for r in range(g.height):
        for c in range(g.width):
            v = grid[r][c]
            if v == 0:
                continue
            cell = g.data[r][c]
            cell.set(v)
            propagate(g, cell, pq)
    return g, pq
