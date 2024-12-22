# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections
# x and y are independent, so we just run 1D line sweep twice
# note: if you have a template, merge intervals might be easier

def checkValidCuts(n: int, rectangles: list[list[int]]) -> bool:
    def works(events):
        events.sort()
        cur = 0
        res = 0
        idx = 0
        while idx < len(events):
            pos = events[idx][0]
            # process all events at this point
            while idx < len(events) and pos == events[idx][0]:
                cur += events[idx][1]
                idx += 1
            if cur == 0:
                res += 1

        return res >= 3  # ignore cut at the end

    v_events = []
    h_events = []
    for x1, y1, x2, y2 in rectangles:
        v_events.append((y1 + 1, 1))
        v_events.append((y2, -1))
        h_events.append((x1 + 1, 1))
        h_events.append((x2, -1))

    return works(h_events) or works(v_events)


print(checkValidCuts(n=5, rectangles=[[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]))
print(checkValidCuts(n=4, rectangles=[[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]))
print(checkValidCuts(n=4, rectangles=[[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]))
