# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
# interval merging problem

from sortedcontainers import SortedList


class SummaryRanges:
    def __init__(self):
        self.inf = inf = 1 << 30
        self.intervals = SortedList([[-inf, -inf], [inf, inf]])

    def addNum(self, value: int) -> None:
        pos = self.intervals.bisect_left([value, self.inf]) - 1  # find position of where to insert interval

        if self.intervals[pos][0] <= value <= self.intervals[pos][1]:  # element already exists
            return

        prev_l, prev_r = self.intervals[pos]
        next_l, next_r = self.intervals[pos + 1]
        if prev_r == value - 1 and next_l == value + 1:  # adding current element combines 2 intervals
            del self.intervals[pos + 1]
            del self.intervals[pos]
            self.intervals.add([prev_l, next_r])

        elif prev_r == value - 1:  # extend by 1
            self.intervals[pos][1] += 1

        elif next_l == value + 1:  # extend by 1
            self.intervals[pos + 1][0] -= 1

        else:  # individual element
            self.intervals.add([value, value])

    def getIntervals(self) -> list[list[int]]:
        return list(self.intervals)[1:-1]  # exclude first and last elements (padding)
