import heapq


def findKthLargest(nums, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    for i in range(k, len(nums)):
        heapq.heappushpop(heap, nums[i])  # an alternative is testing if nums[i] > heap[0]: use heapreplace()
    return heap[0]
