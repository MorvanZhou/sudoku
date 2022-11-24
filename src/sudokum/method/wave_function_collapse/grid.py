import typing as tp

from sudokum.method.wave_function_collapse.cell import Cell


class Grid:
    def __init__(self):
        self.data: tp.List[tp.List[Cell]] = []
        self.max_number = 9
        self.height = self.max_number
        self.width = self.max_number

        for r in range(self.height):
            row = []
            for c in range(self.width):
                row.append(Cell(r, c, max_number=self.max_number))
            self.data.append(row)

    def to_number(self) -> tp.List[tp.List[int]]:
        m = []
        for r in range(self.height):
            row = []
            for c in range(self.width):
                row.append(self.data[r][c].value)
            m.append(row)
        return m

    def __str__(self):
        return "\n".join(
            [" ".join([
                str(self.data[r][c].value) for c in range(self.width)
            ]) for r in range(self.height)])

    def __repr__(self):
        return self.__str__()
