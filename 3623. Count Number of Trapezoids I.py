# https://leetcode.com/problems/count-number-of-trapezoids-i
# Simple combinatorics
# For every pair in each row, match with pairs in all previous rows
# Note: we avoid matching every row and dividing by 2 to avoid mod inverse
# TC: O(n)

from collections import Counter


def countTrapezoids(points: list[list[int]]) -> int:
    MOD = 10 ** 9 + 7

    y_points = Counter()  # number of points in each row
    for x, y in points:
        y_points[y] += 1

    pairs = [row * (row - 1) // 2 for row in y_points.values()]  # pairs in each row
    total = 0
    prev = 0
    for p in pairs:
        total = (total + p * prev) % MOD  # match current row with previous ones
        prev += p

    return total


print(countTrapezoids(points=[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
print(countTrapezoids(points=[[0, 0], [1, 0], [0, 1], [2, 1]]))
