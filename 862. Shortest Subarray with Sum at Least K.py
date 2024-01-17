# ⭐ hard question, worth reviewing
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
# monotonic queue with prefix sum
#
# for each index, we want to remove as many prefix elements as possible to reduce the subarray's size
# however, we must also ensure that the remaining elements still sum up to more than k
# similar to first greater element (also uses deque)

from collections import deque


def shortestSubarray(nums: list[int], k: int) -> int:
    q = deque([(0, -1)])  # (prefix sum up to index (inclusive), index)
    cur = 0
    res = float('inf')

    for right in range(len(nums)):
        cur += nums[right]
        while q and cur - q[0][0] >= k:  # remove extra elements so the remaining is still more than k
            res = min(res, right - q.popleft()[1])

        # remove > elements since we might as well remove everything up to the current if it will result in a GREATER
        # sum, note the >= because even if we remove the same amount, it is more optimal to remove more elements
        while q and q[-1][0] >= cur:
            q.pop()
        q.append((cur, right))  # add the current prefix as an option to remove

    return res if res != float('inf') else -1


print(shortestSubarray(nums = [1], k = 1))
