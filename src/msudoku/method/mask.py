import copy
import random

from msudoku.method.types import ListGrid


def mask(grid: ListGrid, rate: float = 0.5) -> ListGrid:
    if rate > 1.:
        raise ValueError("mask rate should less or equal to 1")
    grid = copy.deepcopy(grid)
    if rate <= 0.:
        return grid

    h = len(grid)
    w = len(grid[0])
    n = h * w
    masked_n = int(n * rate)
    mask_array = [True] * masked_n + [False] * (n - masked_n)
    random.shuffle(mask_array)
    for r in range(h):
        for c in range(w):
            if mask_array[r * w + c]:
                grid[r][c] = 0
    return grid
