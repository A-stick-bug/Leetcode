# https://leetcode.com/problems/length-of-the-longest-increasing-path/
# 2D LIS problem where both dimensions have to be increasing
# Sort by first dimension and use LIS on the other
# Explanation of main code in https://leetcode.com/problems/russian-doll-envelopes
# similar question: https://atcoder.jp/contests/abc369/tasks/abc369_f

from bisect import bisect_left, bisect_right


def maxPathLength(coordinates: list[list[int]], k: int) -> int:
    def maxEnvelopes(envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # first sort by width, then by height
        lis = []

        for i, (width, height) in enumerate(envelopes):
            pos = bisect_left(lis, height)
            if pos == len(lis):  # new envelope in sequence
                lis.append(height)
            else:
                lis[pos] = height

        return len(lis)

    mi, mj = coordinates[k]  # process everything before and after independently
    group1 = [[i, j] for i, j in coordinates if i < mi and j < mj]
    group2 = [[i, j] for i, j in coordinates if i > mi and j > mj]

    return maxEnvelopes(group1) + maxEnvelopes(group2) + 1


print(maxPathLength(coordinates=[[3, 1], [2, 2], [4, 1], [0, 0], [5, 3]], k=1))
print(maxPathLength(coordinates=[[2, 1], [7, 0], [5, 6]], k=2))
