import logging

try:
    import numpy as np
except ModuleNotFoundError:
    import subprocess
    import sys

    print("Dependency not found, try installing numpy>=1.19.5")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy>=1.19.5"])

from sudokum.method.mask import mask
from sudokum.method.types import ListGrid


def generate(mask_rate=0.5) -> ListGrid:
    attempt = 1
    while True:
        n = 9
        g = np.zeros((n, n), np.uint)
        rg = np.arange(1, n + 1)
        g[0, :] = np.random.choice(rg, n, replace=False)
        try:
            for r in range(1, n):
                for c in range(n):
                    col_rest = np.setdiff1d(rg, g[:r, c])
                    row_rest = np.setdiff1d(rg, g[r, :c])
                    avb1 = np.intersect1d(col_rest, row_rest)
                    sub_r, sub_c = r // 3, c // 3
                    avb2 = np.setdiff1d(np.arange(0, n + 1),
                                        g[sub_r * 3:(sub_r + 1) * 3, sub_c * 3:(sub_c + 1) * 3].ravel())
                    avb = np.intersect1d(avb1, avb2)
                    g[r, c] = np.random.choice(avb, size=1)
            break
        except ValueError:
            attempt += 1
    g_list: ListGrid = g.tolist()
    if attempt > 1:
        logging.debug(f"generate by np_union attempt {attempt}")
    return mask(g_list, mask_rate)
