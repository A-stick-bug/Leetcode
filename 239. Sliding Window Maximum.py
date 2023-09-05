# we want the MAXIMUM element in each window, so we use a decreasing monotonic queue

from collections import deque


def maxSlidingWindow(nums, k):
    n = len(nums)
    window = deque()  # keep track of window indices
    result = []
    left = 0

    for right in range(n):
        # decreasing queue: remove until the last element in window ISN'T less than current element
        while window and window[-1] < nums[right]:
            window.pop()
        window.append(nums[right])

        # only check if window is full, otherwise keep incrementing right
        window_size = right - left + 1
        if window_size == k:
            result.append(window[0])  # window[0] is always the largest as smaller ones were removed already

            if window[0] == nums[left]:  # remove max element as it is no longer in the window
                window.popleft()

            # shift window
            left += 1

    return result


# similar solution that stores indices in the queue instead of the actual value
def solution2(nums, k):
    n = len(nums)
    window = deque()
    res = []
    left = 0

    for right in range(n):
        while window and nums[window[-1]] < nums[right]:
            window.pop()
        window.append(right)

        size = right - left + 1
        if size == k:
            res.append(nums[window[0]])

            if window[0] == left:
                window.popleft()
            left += 1

    return res
