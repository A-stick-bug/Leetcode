# create a 2D prefix sum (we have to remove the overlap) in the constructor, so it can be reused
# when accessing the prefix sum, we have to add back the overlap
# as it is  removed twice in " - self.psa[row1][col2 + 1] - self.psa[row2 + 1][col1]"

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.psa = [[0] * (m + 1) for _ in range(n + 1)]  # extra row and column to prevent out of bounds
        for i in range(n):
            for j in range(m):
                self.psa[i + 1][j + 1] = self.psa[i][j + 1] + self.psa[i + 1][j] + matrix[i][j] - self.psa[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.psa[row2 + 1][col2 + 1] + self.psa[row1][col1] - self.psa[row1][col2 + 1] - self.psa[row2 + 1][col1]
