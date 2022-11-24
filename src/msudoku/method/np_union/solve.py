import typing as tp

try:
    import numpy as np
except ModuleNotFoundError:
    import subprocess
    import sys

    print("Dependency not found, try installing numpy>=1.19.5")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy>=1.19.5"])

from msudoku.method.types import ListGrid


def solve(grid: ListGrid, max_try: int = 10) -> tp.Tuple[bool, ListGrid]:
    m = np.array(grid)
    rg = np.arange(m.shape[0] + 1)
    count = 0
    ok = True
    while True:
        mt = m.copy()
        while True:
            d = []
            d_len = []
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if mt[i, j] == 0:
                        possibles = np.setdiff1d(rg, np.union1d(np.union1d(mt[i, :], mt[:, j]),
                                                                mt[3 * (i // 3):3 * (i // 3 + 1),
                                                                3 * (j // 3):3 * (j // 3 + 1)]))
                        d.append([i, j, possibles])
                        d_len.append(len(possibles))
            if len(d) == 0:
                break
            idx = np.argmin(d_len)
            i, j, p = d[idx]
            if len(p) > 0:
                num = np.random.choice(p)
            else:
                break
            mt[i, j] = num
            if len(d) == 0:
                break
        if np.all(mt != 0):
            break
        if count >= max_try:
            ok = False
            break
    return ok, mt
