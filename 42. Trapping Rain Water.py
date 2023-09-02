# using prefix and suffix maximum (simpler than stacks)

from typing import List


def trap(height: List[int]) -> int:
    n = len(height)
    prev, after = [0] * n, [0] * n
    prev[0], after[-1] = height[0], height[-1]  # starting values for prefix and suffix max

    # create prefix and suffix arrays
    for i in range(1, n):
        prev[i] = max(height[i], prev[i - 1])
    for i in reversed(range(n - 1)):
        after[i] = max(height[i], after[i + 1])

    # get amount of water stored based on left and right maximums
    res = 0
    for i in range(n):
        water = min(after[i], prev[i])  # can fill up to min(left, right)

        # we must minus the number of block under
        res += water - height[i]

    return res


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
