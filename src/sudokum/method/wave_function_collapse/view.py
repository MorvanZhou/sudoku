import time
import tkinter as tk

from sudokum.checker import check
from sudokum.method.wave_function_collapse.generate import propagate, pop_cell, reset


class Generation(tk.Tk):
    unit = 80

    def __init__(self):
        super().__init__()
        self.grid, self.pq = reset()
        self.width_group = 3
        self.height_group = 3
        self.max_number = 9
        self.possible_numbers = []

        self.width = self.grid.width * self.unit
        self.height = self.grid.height * self.unit
        self.title("Sudoku")
        self.geometry('{0}x{1}'.format(self.width, self.height))
        self.resizable = False
        self._build()

    def _build(self):
        self.canvas = tk.Canvas(
            self, bg='white', height=self.height, width=self.width)

        # create grids
        for i, c in enumerate(range(0, self.width, self.unit)):
            x0, y0, x1, y1 = c, 0, c, self.height
            self.canvas.create_line(x0, y0, x1, y1, fill="black", width=3 if i % self.width_group == 0 else 1)
        for i, r in enumerate(range(0, self.height, self.unit)):
            x0, y0, x1, y1 = 0, r, self.width, r
            self.canvas.create_line(x0, y0, x1, y1, fill="black", width=3 if i % self.height_group == 0 else 1)

        # add numbers
        for r, y_ in enumerate(range(0, self.height, self.unit)):
            row = []
            for c, x_ in enumerate(range(0, self.width, self.unit)):
                x, y = x_ + self.unit / 2, y_ + self.unit / 2
                text_id = self.canvas.create_text(
                    x, y, text=" ".join([str(i) for i in self.grid.data[r][c].possibilities]),
                    width=self.unit - 12, fill="black", anchor=tk.CENTER, font=('Arial', 20),
                )
                row.append(text_id)
            self.possible_numbers.append(row)
        self.canvas.bind("<Button-1>", self.on_click)
        # pack all
        self.canvas.pack()

    def _render(self, row, col):
        for r in range(self.grid.height):
            for c in range(self.grid.width):
                text_id = self.possible_numbers[r][c]
                cell_ = self.grid.data[r][c]
                if cell_.collapsed():
                    text = str(cell_.value)
                    font = ('Arial', 70)
                else:
                    text = " ".join([str(i) for i in cell_.possibilities])
                    font = ('Arial', 20)
                if r == row and c == col:
                    fill = "blue"
                else:
                    fill = "black"
                self.canvas.itemconfig(text_id, text=text, font=font, fill=fill)


class HumanGeneration(Generation):
    def __init__(self):
        super(HumanGeneration, self).__init__()
        self.valid = True

    def on_click(self, event):
        if not self.valid:
            return
        r, c = event.y // self.unit, event.x // self.unit
        cell = self.grid.data[r][c]
        cell.random_set()
        propagate(self.grid, cell, self.pq)
        self._render(r, c)
        ok, pos = check(self.grid.to_number())
        if not ok:
            for p in pos:
                text_id = self.possible_numbers[p[0]][p[1]]
                self.canvas.itemconfig(text_id, fill="red")
            print("grid not valid, try restarting")


class WaveFunctionCollapseGeneration(Generation):
    def __init__(self):
        super(WaveFunctionCollapseGeneration, self).__init__()

    def on_click(self, event):
        self.move()

    def move(self):
        try:
            cell = pop_cell(self.grid, self.pq)
        except KeyError:
            ok, pos = check(self.grid.to_number())
            if not ok:
                for p in pos:
                    text_id = self.possible_numbers[p[0]][p[1]]
                    self.canvas.itemconfig(text_id, fill="red")
                print("grid not valid, try restarting")
                self.grid, self.pq = reset()
                return "retry"
            return "done"
        cell.random_set()
        propagate(self.grid, cell, self.pq)
        self._render(cell.row, cell.col)

    def render(self):
        res = "continue"
        while True:
            self.update()
            if res == "done":
                break
            elif res == "retry":
                time.sleep(1)
            time.sleep(0.1)
            res = self.move()
        time.sleep(5)
        print("final solution:")
        print(self.grid)
        self.destroy()


def display(human=True):
    if human:
        win = HumanGeneration()
    else:
        win = WaveFunctionCollapseGeneration()
        win.render()
    win.mainloop()
