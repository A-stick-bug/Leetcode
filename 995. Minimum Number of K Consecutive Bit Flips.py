"""
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
Greedy idea with difference array
As soon as we see a 0, we flip it along with the next K-1 bits
We can use a difference array to keep track of which bits are flipped
Note: ^=1 flips a bit
"""


def minKBitFlips(nums: list[int], k: int) -> int:
    n = len(nums)
    diff = [0] * (n + 1)
    cur = 0  # running sum of difference array
    flips = 0
    for i in range(n):
        cur ^= diff[i]  # update running sum on difference array
        nums[i] ^= cur
        # only flip range if needed and it is a valid subarray
        if nums[i] == 0 and i + k <= n:
            cur ^= 1  # update running sum
            nums[i] ^= 1
            diff[i] ^= 1  # update difference array
            diff[i + k] ^= 1
            flips += 1

    return flips if all(i == 1 for i in nums) else -1


print(minKBitFlips(nums=[0, 1, 0], k=1))  # 2
print(minKBitFlips(nums=[1, 1, 0], k=2))  # -1
print(minKBitFlips(nums=[0, 0, 0, 1, 0, 1, 1, 0], k=3))  # 3
