import typing as tp
import random
import logging

from msudoku.method.wave_function_collapse.cell import Cell
from msudoku.method.wave_function_collapse.grid import Grid
from msudoku.method.wave_function_collapse.pq import PriorityQueue
from msudoku.method.types import ListGrid
from msudoku.method.mask import mask
from msudoku import checker


def generate(mask_rate=0) -> ListGrid:
    grid, pq = reset()
    attempt = 1
    while True:
        result = grid.to_number()
        ok, _ = checker.check(result)
        if not ok:
            grid, pq = reset()
            attempt += 1
        done = wave_function_collapse(grid, pq)
        if done:
            break
    masked = mask(result, mask_rate)
    if attempt > 1:
        logging.debug(f"generate by wfc attempt {attempt}")
    return masked


def reset() -> tp.Tuple[Grid, PriorityQueue]:
    grid = Grid()
    pq = PriorityQueue()
    rows = list(range(grid.height))
    cols = list(range(grid.width))
    random.shuffle(rows)
    random.shuffle(cols)
    for r in rows:
        for c in cols:
            pq.put((r, c), grid.max_number)
    return grid, pq


def hold_not_collapsed(grid: Grid, hold: PriorityQueue, row: int, col: int):
    cell = grid.data[row][col]
    if not cell.collapsed():
        hold.put((cell.row, cell.col), cell.entropy)


def propagate(grid: Grid, cell: Cell, pq: PriorityQueue):
    hold = PriorityQueue()
    for r_ in range(grid.height):
        if cell.row == r_:
            for c_ in range(grid.width):
                hold_not_collapsed(grid, hold, r_, c_)
        hold_not_collapsed(grid, hold, r_, cell.col)

    area_row = cell.row // 3
    area_col = cell.col // 3
    for r_ in range(area_row * 3, (area_row + 1) * 3):
        for c_ in range(area_col * 3, (area_col + 1) * 3):
            if cell.row == r_ or cell.col == c_:
                continue
            hold_not_collapsed(grid, hold, r_, c_)

    while True:
        try:
            row, col = hold.pop()
        except KeyError:
            break
        cell_ = grid.data[row][col]
        reduce_possibility = cell_.collapse(cell.value)
        if cell_.collapsed():
            propagate(grid, cell_, pq)
            try:
                pq.remove((row, col))
            except KeyError:
                pass
        elif reduce_possibility:
            pq.put((row, col), cell_.entropy)


def pop_cell(grid: Grid, pq: PriorityQueue) -> Cell:
    (r, c) = pq.pop()
    cell = grid.data[r][c]
    return cell


def wave_function_collapse(grid, pq) -> bool:
    try:
        cell = pop_cell(grid, pq)
    except KeyError:
        return True
    cell.random_set()
    propagate(grid, cell, pq)
    return False
