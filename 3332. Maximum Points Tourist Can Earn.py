# https://leetcode.com/problems/maximum-points-tourist-can-earn
# The question literally gives you the dp state transitions
# Just implement it, add memoization to reduce time complexity to O(n^3), assuming n=k

from functools import cache


def maxScore(n: int, k: int, stayScore: list[list[int]], travelScore: list[list[int]]) -> int:
    @cache
    def solve(i, curr):
        if i >= k:
            return 0
        b = stayScore[i][curr] + solve(i + 1, curr)
        for dest in range(n):
            if dest == curr:
                continue
            b = max(b, travelScore[curr][dest] + solve(i + 1, dest))
        return b

    best = 0
    for start in range(n):
        best = max(best, solve(0, start))
    return best


print(maxScore(n=2, k=1, stayScore=[[2, 3]], travelScore=[[0, 2], [1, 0]]))
print(maxScore(n=3, k=2, stayScore=[[3, 4, 2], [2, 1, 2]], travelScore=[[0, 2, 1], [2, 0, 4], [3, 2, 0]]))
