from typing import List


class NumMatrix(object):
    def __init__(self, matrix):
        self.M, self.N = len(matrix), len(matrix[0])
        self.mat = [[0] * self.N for _ in range(self.M)]  # 0-indexed
        self.BIT = [[0] * (self.N + 1) for _ in range(self.M + 1)]  # 1-indexed
        for i in range(self.M):
            for j in range(self.N):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        row += 1  # change to 1-indexing
        col += 1
        diff = val - self.mat[row - 1][col - 1]
        self.mat[row - 1][col - 1] = val
        while row <= self.M:
            c = col
            while c <= self.N:
                self.BIT[row][c] += diff
                c += c & (-c)
            row += row & (-row)

    def query(self, row, col):
        row += 1  # change to 1-indexing
        col += 1
        res = 0
        while row:
            c = col
            while c:
                res += self.BIT[row][c]
                c -= c & (-c)
            row -= row & (-row)
        return res

    def sumRegion(self, row1, col1, row2, col2):
        # query in the same way as 2D prefix sum
        return self.query(row2, col2) + \
            self.query(row1 - 1, col1 - 1) - \
            self.query(row1 - 1, col2) - \
            self.query(row2, col1 - 1)
