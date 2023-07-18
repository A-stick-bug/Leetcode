from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
    total = 0
    cols = len(mat[0])
    for i in range(len(mat)):
        total += mat[i][i] + mat[i][cols-i-1]
    return total
