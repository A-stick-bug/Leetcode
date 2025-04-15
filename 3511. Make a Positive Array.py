# https://leetcode.com/problems/make-a-positive-array/
# Prefix sums + range update on all existing values (offsetting)
# TC: O(n)

from itertools import accumulate


def makeArrayPositive(nums: list[int]) -> int:
    n = len(nums)
    inf = 1 << 30
    psa = [0] + list(accumulate(nums))

    prefix = inf  # minimum of subarrays of length >2 ending at i
    shift_val = 0
    total = 0
    up_to = 1  # indices processed up to here

    for i in range(n):
        if i <= up_to:  # already processed
            continue

        shift_val += nums[i]
        prefix = min(prefix, psa[i + 1] - psa[i - 2] - shift_val)

        if prefix + shift_val <= 0:
            total += 1
            prefix = inf
            shift_val = 0
            up_to = i + 2

    return total


print(makeArrayPositive([-5, 4, 2, -2, 2, 4, -5]))
print(makeArrayPositive([-1, -2, 3, -1, 2, 6]))

print(makeArrayPositive([5, -2, 4, -3]))
print(makeArrayPositive([-1, -2, -3]))
