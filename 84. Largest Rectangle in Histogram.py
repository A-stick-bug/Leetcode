# strictly increasing monotonic stack
# previous smaller problem

from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    heights.append(0)  # this will make sure we check remaining elements in stack after iterating all heights
    stack = []
    res = 0
    for i in range(len(heights)):

        # keep stack in increasing order (strict)
        while stack and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]

            # if the stack is empty, then the current height can extend all the way to the left
            width = i if not stack else i - stack[-1] - 1  # minus one because it is the width between 2 points
            res = max(res, height * width)  # check the maximum area we can obtain with current height

        stack.append(i)

    return res


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
