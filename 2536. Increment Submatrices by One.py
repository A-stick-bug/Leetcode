# queries are 0-indexed, difference array is 1-indexed
# build a 2D difference array using the principle of inclusion and exclusion
# O(n^2 + q), O(1) per query, n^2 to turn 2d difference array into regular array

from typing import List


def rangeAddQueries(n: int, queries: List[List[int]]) -> List[List[int]]:
    diff = [[0] * (n + 2) for _ in range(n + 2)]  # surround the entire array with 0s to prevent index out of bounds
    for r1, c1, r2, c2 in queries:
        diff[r1 + 1][c1 + 1] += 1
        diff[r2 + 2][c2 + 2] += 1
        diff[r2 + 2][c1 + 1] -= 1
        diff[r1 + 1][c2 + 2] -= 1

    # convert difference array into regular array using 2D prefix sum method
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]

    diff =  diff[1:-1]  # remove top and bottom row
    diff = [row[1:-1] for row in diff]  # remove first row and column
    return diff

print(rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]]))
