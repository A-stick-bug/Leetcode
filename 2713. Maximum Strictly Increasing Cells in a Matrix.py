"""
https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/
Q: DP, Find longest strictly increasing path in a matrix

- Basically the matrix can be thought of as a DAG
- DP states: [row][col] longest path ending here, Transition: all cells in the same row or column
- Notice how there are too many previous values to do the state transition efficiently

Key observation -> optimization:
Lets say our matrix is just a row [1, 2, 5, 5, 9] and we are currently on 5
In this case, we can transition from anything except numbers that are >=5
- to avoid transitioning from numbers >5, simply fill in the table in increasing order of value
- for numbers =5 however, we must put them all in a temporary storage and only update the max of their
  respective rows and columns if the current numbers is >5

TC: O(MNlog(MN)) from sorting to fill table in order of increasing value.
"""


def maxIncreasingCells(mat: list[list[int]]) -> int:
    n, m = len(mat), len(mat[0])
    cells = [(mat[i][j], i, j) for i in range(n) for j in range(m)]
    cells.sort(key=lambda x: x[0])  # sort by value

    rows = [0] * n  # rows[i]: max(dp[i]), note that the numbers only get bigger as we fill in more states
    cols = [0] * m
    dp = [[0] * m for _ in range(n)]
    waiting = []
    for val, i, j in cells:
        while waiting and waiting[0][0] < val:  # we can now transition from anything less than val so update the max
            _, r, c = waiting.pop()
            rows[r] = max(rows[r], dp[r][c])
            cols[c] = max(cols[c], dp[r][c])

        dp[i][j] = max(rows[i], cols[j]) + 1  # transition from max element in the same row/col
        waiting.append((val, i, j))  # put in temporary storage

    return max(max(r) for r in dp)


print(maxIncreasingCells(mat=[[3, 1], [3, 4]]))
print(maxIncreasingCells(mat=[[1, 1], [1, 1]]))
print(maxIncreasingCells(mat=[[3, 1, 6], [-9, 5, 7]]))
print(maxIncreasingCells(mat=[[-4, 8, -3, 2, -4, -8, 7, 5, -2],
                              [-5, 5, -7, -2, 6, -6, -8, -4, -4]]))
