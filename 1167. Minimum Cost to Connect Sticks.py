import heapq

def connectSticks(sticks):
    res = 0
    heapq.heapify(sticks)
    while len(sticks) > 1:
        x = heapq.heappop(sticks)
        y = heapq.heappop(sticks)
        res += x + y
        heapq.heappush(sticks, x+y)
    return res


print(connectSticks([1,8,3,5]))
