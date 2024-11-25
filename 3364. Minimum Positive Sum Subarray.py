# brute force

def minimumSumSubarray(nums: list[int], l: int, r: int) -> int:
    ans = float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = sum(nums[i:j + 1])
            if l <= j - i + 1 <= r and sub > 0:
                ans = min(ans, sub)
    return ans if ans != float('inf') else -1
