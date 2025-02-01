# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i
# Sliding window approach, window size = k + 1
# The max contiguous we can get from a window is (length - sum of interval lengths inside)
# We can think of this as putting all intervals in the window next to each other


def maxFreeTime(eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
    removed = 0
    startTime = [0] + startTime + [eventTime]
    endTime = [0] + endTime + [eventTime]

    best = 0
    for i, (s, e) in enumerate(zip(startTime, endTime)):
        removed += e - s

        li = i - (k + 1)
        if li >= 0:
            removed -= endTime[li] - startTime[li]
            cur_le = e - endTime[li] - removed
            best = max(best, cur_le)

    return best


print(maxFreeTime(eventTime=19, k=2, startTime=[1, 5, 11, 14], endTime=[3, 7, 13, 17]))
print(maxFreeTime(eventTime=5, k=1, startTime=[1, 3], endTime=[2, 5]))
print(maxFreeTime(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10]))
print(maxFreeTime(eventTime=5, k=2, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]))
