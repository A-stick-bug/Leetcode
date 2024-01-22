def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    res = [intervals[0]]
    for l, r in intervals[1:]:
        if res[-1][1] >= l:  # left overlaps with right, we can combine
            res[-1][1] = max(res[-1][1], r)
        else:  # disjoint intervals
            res.append([l, r])

    return res


print(merge(intervals=[[1, 4], [4, 5]]))
