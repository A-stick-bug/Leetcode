# https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/description/
# Mostly observation and some intuition based logic (hard to prove)
# in contest, note that many people solved so it's probably not that complicated
#
# First rule out the impossible case by pigeonhole principle
# It seems like it should always be possible otherwise
# The idea is that we can fix 2 forbidden indices at once by swapping them, UNLESS they have the same value
# - It seems like there is always a way to fix 2 every swap EXCEPT when the majority takes up more than half
# - Here, we always swap(majority, other) and use individual swaps for the rest

from collections import Counter


def minSwaps(nums: list[int], forbidden: list[int]) -> int:
    freq1 = Counter(nums)
    freq2 = Counter(forbidden)
    n = len(nums)

    if any(freq1[k] > n - freq2[k] for k in freq1.keys()):  # not enough spots
        return -1

    mismatch = Counter()  # values of mismatch
    for i in range(n):
        if nums[i] == forbidden[i]:
            mismatch[nums[i]] += 1

    if not mismatch:
        return 0

    most = max(mismatch.values())
    total = sum(mismatch.values())
    if most > total - most:  # majority > half, we can't do 2x swaps at the end
        cost = total - most  # these are the 2x swaps
        most -= total - most
        return cost + most  # add the 1x swaps
    else:
        return (total + 1) // 2  # use 2x swaps, odd parity requires extra move
