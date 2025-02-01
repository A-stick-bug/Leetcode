# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii
# For each interval, check if we can move it somewhere else
# We can od this by maintaining all 'gaps' in a SortedList

from sortedcontainers import SortedList


def maxFreeTime(eventTime: int, startTime: list[int], endTime: list[int]) -> int:
    startTime = [0, 0] + startTime + [eventTime, eventTime]  # padding
    endTime = [0, 0] + endTime + [eventTime, eventTime]

    gaps = SortedList([startTime[i] - endTime[i - 1] for i in range(1, len(endTime))])

    best = 0
    for i in range(1, len(endTime) - 1):
        l = startTime[i] - endTime[i - 1]  # remove gaps right next to this interval
        r = startTime[i + 1] - endTime[i]
        gaps.remove(l)
        gaps.remove(r)

        le = endTime[i] - startTime[i]
        if gaps and le <= gaps[-1]:  # we can move this interval somewhere else
            cur_le = startTime[i + 1] - endTime[i - 1]
        else:  # we cannot move it somewhere else, instead push it to the left to make as much space as possible
            cur_le = startTime[i + 1] - endTime[i - 1] - (endTime[i] - startTime[i])
        best = max(best, cur_le)

        gaps.add(l)  # add the gaps back now that we are done
        gaps.add(r)
    return best


print(maxFreeTime(eventTime=19, startTime=[1, 5, 11, 14], endTime=[3, 8, 13, 17]))

print(maxFreeTime(eventTime=5, startTime=[1, 3], endTime=[2, 5]))
print(maxFreeTime(eventTime=10, startTime=[0, 7, 9], endTime=[1, 8, 10]))
print(maxFreeTime(eventTime=10, startTime=[0, 3, 7, 9], endTime=[1, 4, 8, 10]))
print(maxFreeTime(eventTime=5, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]))
