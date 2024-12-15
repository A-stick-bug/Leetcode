def buttonWithLongestTime(events) -> int:
    mx = events[0][1]
    idx = events[0][0]
    for i in range(1, len(events)):
        t = events[i][1] - events[i - 1][1]
        if t > mx or (t == mx and events[i][0] < idx):
            idx = events[i][0]
            mx = t
    return idx


print(buttonWithLongestTime(events=[[1, 2], [2, 5], [3, 9], [1, 15]]))
print(buttonWithLongestTime(events=[[10, 5], [1, 7]]))
