import typing as tp

import sudokum.method.wave_function_collapse as wfc
from sudokum.checker import check
from sudokum.method import np_union
from sudokum.method.types import ListGrid

_MAP = {
    "wfc": (wfc.generate, wfc.solve),
    "np_union": (np_union.generate, np_union.solve)
}


def generate(mask_rate: float = 0.5, method="wfc") -> ListGrid:
    return _MAP[method][0](mask_rate=mask_rate)


def solve(grid: ListGrid, max_try: int = 10, method="wfc", ) -> tp.Tuple[bool, ListGrid]:
    return _MAP[method][1](grid, max_try)


display_wfc = wfc.display
