# there is alternate O(n) solution that only uses the freq map because the only element that can go above the limit is
# the one at the right
# O(nlogn)

from typing import List
from sortedcontainers import SortedList
from collections import defaultdict

def maxSubarrayLength(nums: List[int], k: int) -> int:
    freq = defaultdict(int)
    left = 0
    window = SortedList()
    res = 0

    for right, num in enumerate(nums):
        if (freq[num], num) in window:  # remove old
            window.remove((freq[num], num))
        freq[num] += 1
        window.add((freq[num], num))

        while window and window[-1][0] > k:
            if (freq[nums[left]], nums[left]) in window:  # remove old
                window.remove((freq[nums[left]], nums[left]))
            freq[nums[left]] -= 1
            window.add((freq[nums[left]], nums[left]))
            left += 1

        res = max(res, right - left + 1)

    return res

print(maxSubarrayLength(nums = [5,5,5,5,5,5,5], k = 4))
