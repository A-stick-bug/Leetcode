from bisect import insort_left

# heap is better for this because insort_left takes O(n) time
def lastStoneWeight(stones):
    stones.sort()
    while stones:
        # get heaviest
        first = stones.pop()

        # last stone remaining
        if not stones:
            return first
        second = stones.pop()

        if first > second:
            insort_left(stones,first-second)
    return 0