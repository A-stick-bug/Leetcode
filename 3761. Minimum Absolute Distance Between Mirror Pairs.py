# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs
# For each index, find the nearest index to the right equal to the reverse
# We loop right to left, tracking the most recent index for each number
# TC: O(n)

def minMirrorPairDistance(nums: list[int]) -> int:
    def rev(num):
        return int(str(num)[::-1])

    nxt = {}  # most recent location for each number

    n = len(nums)
    best = n + 1
    for i in reversed(range(n)):
        target = rev(nums[i])
        if target in nxt:
            best = min(best, nxt[target] - i)
        nxt[nums[i]] = i

    if best == n + 1:
        return -1
    else:
        return best
