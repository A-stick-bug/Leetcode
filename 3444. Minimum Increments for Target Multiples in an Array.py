# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array
# Bitmask DP
# Only take the top 4 from each possible mask
# For each number, consider the cost required to make it reach a subset of targets
# TC: O(2^(2^m) + 2^m * n)

from math import lcm


def minimumIncrements(nums: list[int], target: list[int]) -> int:
    n = len(nums)
    m = len(target)
    inf = 1 << 30

    choices = [[0] * (1 << m) for _ in range(n)]
    for i in range(n):
        for mask in range(1, 1 << m):
            val = nums[i]
            mul = 1
            for bit in range(m):
                if mask & (1 << bit):
                    mul = lcm(mul, target[bit])
            if val % mul == 0:
                choices[i][mask] = 0
            else:
                choices[i][mask] = (val // mul + 1) * mul - val

    # take top 4 for each mask, max of 64
    using = []
    for j in range(1 << m):
        if not choices:
            break
        choices.sort(key=lambda x: x[j], reverse=True)
        for _ in range(m):
            if choices:
                using.append(choices.pop())

    le = len(using)
    cache = [[-1] * (1 << m) for _ in range(le)]

    def solve(idx, mask):
        if mask == (1 << m) - 1:  # all targets reached
            return 0
        if idx == le:  # out of masks
            return inf
        if cache[idx][mask] != -1:
            return cache[idx][mask]
        best = inf
        for take in range(1 << m):
            best = min(best, solve(idx + 1, mask | take) + using[idx][take])
        cache[idx][mask] = best
        return best

    return solve(0, 0)


print(minimumIncrements([4, 8, 9, 1, 1, 9, 10, 7], [10, 10, 2, 2]))
print(minimumIncrements(nums=[1, 2, 3], target=[4]))
print(minimumIncrements(nums=[8, 4], target=[10, 5]))
print(minimumIncrements(nums=[7, 9, 10], target=[7]))
