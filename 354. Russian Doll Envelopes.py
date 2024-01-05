# https://leetcode.com/problems/russian-doll-envelopes
# 2D LIS DP, first sort by the width to reduce to 1D, then find the LIS based on the height
#
# Note that if 2 envelopes have the same width/height, we cannot put them inside each other
# Therefore, we need to REVERSE sort the height to prevent duplicate widths in the LIS

from bisect import bisect_left


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


print(maxEnvelopes([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]))
