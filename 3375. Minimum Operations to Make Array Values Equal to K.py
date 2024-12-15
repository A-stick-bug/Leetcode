# simple logic

def minOperations(nums: list[int], k: int) -> int:
    if any(i < k for i in nums):
        return -1

    nums.sort()
    res = list(set([i for i in nums if i >= k]))
    if k in res:
        return len(res) - 1
    else:
        return len(res)


print(minOperations(nums=[5, 2, 5, 4, 5], k=2))
print(minOperations(nums=[2, 1, 2], k=2))
print(minOperations(nums=[9, 7, 5, 3], k=1))
