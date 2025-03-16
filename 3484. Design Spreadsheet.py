from collections import defaultdict


class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = defaultdict(lambda: defaultdict(int))

    def _get_cell(self, cell):
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:])
        return self.grid[col][row]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:])
        self.grid[col][row] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:])
        self.grid[col][row] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        if a.isnumeric():
            a = int(a)
        else:
            a = self._get_cell(a)
        if b.isnumeric():
            b = int(b)
        else:
            b = self._get_cell(b)
        return a + b
