# basic implementation

def hasIncreasingSubarrays(nums: list[int], k: int) -> bool:
    n = len(nums)
    for i in range(n - k + 1):
        j = i + k
        if j + k <= n:
            s1 = nums[i:i + k]
            s2 = nums[j:j + k]
            if all(s1[k - 1] < s1[k] for k in range(1, len(s1))) and all(s2[k - 1] < s2[k] for k in range(1, len(s2))):
                return True
    return False


print(hasIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k=3))
print(hasIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5))
