"""
https://leetcode.com/problems/the-skyline-problem/description/
Q: Given rectangles (with fixed base), find all points where the height changes
A: Line sweep with a sorted structure to get maximum

- At each position x, handle every event with that x value
- Then, get the current maximum height and see if it is different from the previous

"""
from sortedcontainers import SortedList


def getSkyline(buildings: list[list[int]]) -> list[list[int]]:
    events = []
    for start, end, height in buildings:  # extract all events for line sweep
        events.append((start, height))
        events.append((end, -height))
    events.sort(key=lambda x: x[0])  # sort by x

    res = [[-1, -1]]  # padding to prevent index error
    heights = SortedList([0])  # start at 0, currently there are no buildings
    i = 0
    while i < len(events):
        x = events[i][0]
        while i < len(events) and events[i][0] == x:  # process all events with same x value
            h = events[i][1]
            if h > 0:
                heights.add(h)  # start of rectangle
            else:
                heights.remove(-h)  # end of rectangle
            i += 1

        highest = heights[-1]
        if res[-1][1] == highest:  # no height change
            continue
        else:  # height change at current x value
            res.append([x, highest])

    return res[1:]


print(getSkyline(buildings=[[1, 2, 1], [1, 2, 2], [1, 2, 3]]))
