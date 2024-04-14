"""
https://leetcode.com/problems/3sum/description/

Solution 1: N^2 with dict, TLE
Solution 2: fix 1 element and use 2 pointers, AC
"""

from collections import defaultdict


def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    nums.sort()  # must sort to do 2-pointers
    res = set()
    used = set()

    for i in range(n):  # fix element i, add to 0 with 2 elements after i
        if nums[i] in used:  # optimization to avoid duplicates
            continue
        r = n - 1
        for l in range(i + 1, n):
            while r > l and nums[l] + nums[r] + nums[i] > 0:
                r -= 1
            if r == l:
                break
            if nums[l] + nums[r] + nums[i] == 0:
                res.add(tuple(sorted([nums[l], nums[r], nums[i]])))

        used.add(nums[i])

    return list(map(list, list(res)))


print(threeSum( nums = [-1,0,1,2,-1,-4]))


def threeSum_slow(nums: list[int]) -> list[list[int]]:
    """
    SOLUTION 1
    In 2sum, we learned that we can cut down a factor of N using dict
    We can apply the same logic here where we store value:[pairs (i,j) where i+j=value]
    Note that this has a bad constant factor and will TLE
    """
    target = 0
    n = len(nums)
    res = []

    table = defaultdict(list)
    for i in range(n):
        for i1, i2 in table[target - nums[i]]:
            res.append(tuple(sorted([nums[i], i1, i2])))
        for j in range(i):  # store index pairs
            table[nums[i] + nums[j]].append((nums[i], nums[j]))

    return list(map(list, list(set(res))))
