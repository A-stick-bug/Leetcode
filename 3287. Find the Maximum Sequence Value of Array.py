# https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/
# knapsack DP on bits
# O(n^2 * 2^7),
# O(n): try all split points
# O(n * 2^7): check the [min, max] range of each bitmask

def maxValue(nums: list[int], k: int) -> int:
    MX = 2 ** 7
    best = 0
    inf = 10
    n = len(nums)
    for mid in range(1, n):
        a1 = nums[:mid]
        a2 = nums[mid:]
        if len(a1) < k or len(a2) < k:  # too short
            continue

        # minimum number of values to achieve mask of `i`
        dp1 = [inf] * MX
        dp1[0] = 0  # base case: 0 moves to have nothing
        for val in a1:
            for i in reversed(range(MX)):
                dp1[i | val] = min(dp1[i | val], dp1[i] + 1)

        # max
        dp11 = [-inf] * MX
        dp11[0] = 0
        for val in a1:
            for i in reversed(range(MX)):
                dp11[i | val] = max(dp11[i | val], dp11[i] + 1)

        # min
        dp2 = [inf] * MX
        dp2[0] = 0  # base case: 0 moves to have nothing
        for val in a2:
            for i in reversed(range(MX)):
                dp2[i | val] = min(dp2[i | val], dp2[i] + 1)

        # max
        dp22 = [-inf] * MX
        dp22[0] = 0
        for val in a2:
            for i in reversed(range(MX)):
                dp22[i | val] = max(dp22[i | val], dp22[i] + 1)

        for mask1 in range(1, MX):
            for mask2 in range(1, MX):
                if dp1[mask1] <= k <= dp11[mask1] and dp2[mask2] <= k <= dp22[mask2]:
                    best = max(best, mask1 ^ mask2)

    return best


print(maxValue(nums=[2, 6, 7], k=1))
print(maxValue(nums=[4, 2, 5, 6, 7], k=2))
