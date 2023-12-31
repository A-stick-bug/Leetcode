"""
⭐ DIFFICULT QUESTION
https://leetcode.com/problems/count-of-range-sum/

Keep track of the prefix sums in a sorted list.
For each element, we can now find the minimum number of elements we can not include to have a sum of upper
and the maximum number of elements we can not include to have a sum of lower

"""

from sortedcontainers import SortedList


def countRangeSum(nums: list[int], lower: int, upper: int) -> int:
    sums = SortedList([0])  # zero is there because we can just take the element itself as a range
    cur = 0
    total = 0

    for num in nums:
        cur += num  # add current number to prefix sum

        # (cur-upper) is the stuff we want to remove from before so that after we remove it,
        # we are left with the lower bound
        low = sums.bisect_left(cur - upper)
        high = sums.bisect_right(cur - lower)
        total += high - low

        sums.add(cur)

    return total

print(countRangeSum(nums = [-2,5,-1], lower = -2, upper = 2))
