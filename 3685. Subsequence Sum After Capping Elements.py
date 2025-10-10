# https://leetcode.com/problems/subsequence-sum-after-capping-elements/description/
# bitmask DP with binary packaging
# note: binary packing was probably redundant here
# key idea is to store in-between dp states, so you don't have to recompute from scratch
# TC: O(1/32 * NK), there is no log factor from binary packing as it can only ever improve TC here

def subsequenceSumAfterCapping(nums: List[int], k: int) -> List[bool]:
    n = len(nums)
    freq = [0] * (n + 1)
    for i in nums:
        freq[i] += 1
    mask = (1 << 4003) - 1

    dp = 1
    dps = [dp]
    for i in range(1, n + 1):
        rem = freq[i]
        for j in range(32):
            pack = 1 << j
            if rem >= pack:
                dp |= dp << (pack * i)
                rem -= pack
                dp &= mask
            else:
                dp |= dp << (rem * i)
                dp &= mask
                break

        dps.append(dp)

    ans = []
    acc = 0
    for i in range(1, n + 1):
        dp = dps[i - 1]
        rem = n - acc

        for j in range(32):
            pack = 1 << j
            if rem >= pack:
                dp |= dp << (pack * i)
                rem -= pack
                dp &= mask
            else:
                dp |= dp << (rem * i)
                dp &= mask
                break

        ans.append(bool(dp & (1 << k)))
        acc += freq[i]
    return ans
