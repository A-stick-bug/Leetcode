from collections import deque


def maxSlidingWindow(nums, k):
    n = len(nums)
    q = deque()
    l, r = 0, 0
    res = [0] * (n - k + 1)

    while r < n:
        while q and q[-1] < nums[r]:
            q.pop()
        q.append(nums[r])

        r += 1

        if r - l == k:
            res[l] = q[0]
            if nums[l] == q[0]:
                q.popleft()
            l += 1
    return res
