"""
O(n)
Previous greater element (decreasing stack)
Note: the heights are distinct

Taller people block the ones after it that are shorter
For this example, [10,6,8,5,11,9], index 0 can see 3 because index 2 (8) blocks index 3 (5) from view
"""

from typing import List


def canSeePersonsCount(heights: List[int]) -> List[int]:
    n = len(heights)
    res = [0] * n
    stack = []

    for i in reversed(range(n)):
        can_see = 0  # number of people the current person can see

        # update elements with a lower height than current (decreasing stack)
        while stack and heights[i] > heights[stack[-1]]:
            stack.pop()
            can_see += 1

        if stack:  # there is a person taller than the current, can see 1 extra
            can_see += 1

        res[i] = can_see
        stack.append(i)

    return res


print(canSeePersonsCount([10, 6, 8, 5, 11, 9]))
