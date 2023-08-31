# Next greater element: decreasing monotonic stack (equal is allowed)


from typing import List


def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * len(nums)
    nums *= 2  # double the array because it is circular
    stack = []

    for i, num in enumerate(nums):

        # if the current element is greater, we can set the next greater value for previous elements
        while stack and num > nums[stack[-1]]:
            prev = stack.pop()
            prev %= n  # element i and i+n are the same
            res[prev] = num

        stack.append(i)

    return res
