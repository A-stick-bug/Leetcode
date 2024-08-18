# brute force: O(n^3)

def resultsArray(nums: list[int], k: int) -> list[int]:
    res = []
    n = len(nums)
    for i in range(n - k + 1):
        sub = nums[i:i + k]
        if sub == sorted(sub) and len(sub) == (max(sub) - min(sub) + 1):
            res.append(max(sub))
        else:
            res.append(-1)
    return res


print(resultsArray(nums=[1, 2, 3, 4, 3, 2, 5], k=3))
print(resultsArray(nums=[2, 2, 2, 2, 2], k=4))
print(resultsArray(nums=[3, 2, 3, 2, 3, 2], k=2))
