# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero
# Math + observation
# The number of divisions by 4 it takes to get a number to zero is floor(log4(n)) + 1
# Observation: you will always be able to do 2 simultaneous operations unless the sum is odd
# This is the case since the log4 representation goes up by at most 1 each time

from itertools import accumulate
from collections import Counter

MN = 16  # log4(10^9)
p4 = list(accumulate([0] + [3 * 4 ** i for i in range(MN)]))
covers = [[p4[i] + 1, p4[i + 1]] for i in range(MN)]  # range of floor values


# print(covers)

def minOperations(queries: list[list[int]]) -> int:
    def get_prefix_count(mx):
        freq = Counter()
        for i in range(MN):
            l, r = covers[i]
            if mx >= r:
                freq[i + 1] += r - l + 1  # fully covered
            else:
                freq[i + 1] += mx - l + 1  # partially covered
                break
        return freq

    def get_range_count(l, r):
        return get_prefix_count(r) - get_prefix_count(l - 1)

    ans = []
    for l, r in queries:
        freq = get_range_count(l, r)
        # (number of operations) * (frequency), use ceil division
        ans.append((sum(k * v for k, v in freq.items()) + 1) // 2)

    # print(ans)
    return sum(ans)


print(minOperations(queries=[[1, 2], [2, 4], [2, 6]]))  # 1,2,4

# # code used to make observations
# def count_moves(n):
#     c = 0
#     while n > 0:
#         n = n // 4
#         c += 1
#     return c
#
#
# res = []
# for i in range(1, 100):
#     from math import log, floor
#
#     print(i, count_moves(i), floor(log(i, 4)) + 1)
#     res.append(count_moves(i))
#
# from collections import Counter
#
# print(Counter(res))  # frequencies: [3, 12, 48, ..., 3*4^x]
