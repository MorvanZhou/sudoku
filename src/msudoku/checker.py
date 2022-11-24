import typing as tp


def check(solution: tp.List[tp.List[int]]) -> tp.Tuple[bool, tp.List[tp.Tuple[int, int]]]:
    for r in range(9):
        tmp_set = set()
        dup = []
        for v in solution[r]:
            if v in tmp_set and v != 0:
                dup.append(v)
            tmp_set.add(v)
            if len(dup) > 0:
                pos = [(r, solution[r].index(d)) for d in dup]
                return False, pos

    for c in range(9):
        solution_list = []
        dup = []
        for r in range(9):
            v = solution[r][c]
            if v in solution_list and v != 0:
                dup.append(v)
            solution_list.append(v)
            if len(dup) > 0:
                pos = [(solution_list.index(d), c) for d in dup]
                return False, pos

    for r in range(0, 9, 9 // 3):
        for c in range(0, 9, 9 // 3):
            solution_list = []
            dup = []
            for i in range(9):
                v = solution[r + i // 3][c + i % 3]
                if v in solution_list and v != 0:
                    dup.append(v)
                solution_list.append(v)
                if len(dup) > 0:
                    pos = []
                    for d in dup:
                        i = solution_list.index(d)
                        pos.append((r + i // 3, c + i % 3))
                    return False, pos
    return True, []
