# https://leetcode.com/problems/non-overlapping-intervals/
# this is basically the task scheduling problem (classic greedy)
# except we are counting how many tasks we CAN'T schedule

def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])  # greedy: sort by min R (ends first)

    rt = -100000  # current range is occupied up to here
    removed = 0

    for l, r in intervals:
        if rt <= l:  # not occupied, add current interval
            rt = r
        else:
            removed += 1

    return removed


print(eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
