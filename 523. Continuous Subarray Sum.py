# https://leetcode.com/problems/continuous-subarray-sum
# matching mod values with dict (2-sum method)
# after we build a PSA, if psa[i]%k=x and psa[j]%k=x, (psa[i]-psa[j])%k=0
#
# note that we wait before adding each element to avoid counting subarrays of length 1

from itertools import accumulate


def checkSubarraySum(nums: list[int], k: int) -> bool:
    psa = [0] + list(accumulate(nums))
    match = set()

    waitlist = -1
    for i in psa:
        if i % k in match:
            return True
        match.add(waitlist)
        waitlist = i % k

    return False
