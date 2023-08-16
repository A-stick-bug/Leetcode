from collections import deque


def maxSlidingWindow(nums, k):
    window = deque()  # keep track of window indices
    result = []
    left = right = 0

    while right < len(nums):
        # remove until the last element in window ISN'T less than current element
        while window and window[-1] < nums[right]:
            window.pop()
        window.append(nums[right])

        window_size = right - left + 1
        if window_size < k:  # if less than window size, keep adding elements (while also keeping only the maximum)
            right += 1

        elif window_size == k:  # window is full
            result.append(window[0])  # window[0] is always the largest as smaller ones were removed already
            if window[0] == nums[left]:  # remove max element as it is no longer in the window
                window.popleft()

            # shift window
            left += 1
            right += 1

    return result
