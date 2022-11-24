import random


class Cell:
    def __init__(self, row: int, col: int, max_number: int):
        self.row = row
        self.col = col
        self.possibilities = list(range(1, max_number + 1))
        self.value = 0

    def __str__(self):
        return f"({self.value} {self.possibilities})"

    def __repr__(self):
        return self.__str__()

    def collapse(self, number):
        if self.entropy > 1:
            try:
                self.possibilities.remove(number)
            except ValueError:
                return False
            if self.entropy == 1:
                self.value = self.possibilities[0]
            return True
        return False

    def random_set(self):
        self.set(random.choice(self.possibilities))

    def set(self, v: int):
        if v not in self.possibilities:
            raise ValueError(f"value {v} not in possibilities {self.possibilities}")
        self.value = v
        self.possibilities = [self.value]

    def collapsed(self) -> bool:
        return self.value != 0

    @property
    def entropy(self):
        return len(self.possibilities)
