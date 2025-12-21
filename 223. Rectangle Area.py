# https://leetcode.com/problems/rectangle-area/description/
# Generalized solution that can be extended to work on many rectangles
#
# Simplified line sweep, no data structures needed since there are only 2 rectangles
# Sweep on y-axis, so just rotate the visualization

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    def coverage(intervals):  # get x axis coverage of intervals
        intervals.sort()
        if not intervals:
            return 0
        elif len(intervals) == 1:
            return intervals[0][1] - intervals[0][0]
        else:
            a, b = intervals[0]
            c, d = intervals[1]
            if b >= c:
                return max(b, d) - min(a, c)
            else:
                return (b - a) + (d - c)

    rects = [(ax1, ay1, ax2, ay2), (bx1, by1, bx2, by2)]
    events = []
    for x1, y1, x2, y2 in rects:
        events.append((y1, x1, x2, 1))
        events.append((y2, x1, x2, -1))
    events.sort(key=lambda x: x[0])  # sort by y

    total = 0
    prev_y = -999999
    intervals = []
    for y, x1, x2, delta in events:
        total += (y - prev_y) * coverage(intervals)
        if delta == 1:
            intervals.append((x1, x2))
        else:
            intervals.remove((x1, x2))
        prev_y = y
    return total


print(computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))
print(computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2))
