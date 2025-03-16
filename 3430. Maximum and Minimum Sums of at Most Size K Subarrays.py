# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/description/
# Lots of math and implementation pain (careful on bounds)
# Monotonic stack for previous/next greater/smaller element
# Find sum of piecewise (linear + constant) function with arithmetic sum formula

def minMaxSubarraySum(nums: list[int], k: int) -> int:
    n = len(nums)

    stack = []
    prev_smaller = [-1] * n
    nxt_smaller = [n] * n
    for i, val in enumerate(nums):
        while stack and val <= nums[stack[-1]]:
            nxt_smaller[stack.pop()] = i
        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)

    stack = []
    prev_larger = [-1] * n
    nxt_larger = [n] * n
    for i, val in enumerate(nums):
        while stack and val >= nums[stack[-1]]:
            nxt_larger[stack.pop()] = i
        if stack:
            prev_larger[i] = stack[-1]
        stack.append(i)

    # print(prev_smaller)
    # print(nxt_smaller)
    # print(prev_larger)
    # print(nxt_larger)

    def count_subarrays(l, r, i):
        """
        Count the number of subarrays satisfying:
        - inside [l,r]
        - containing index i
        - having length of at most k
        """

        def range_sum(l, r):  # inclusive sum of integers [l,r]
            # assert l <= r
            if l > r:
                return 0
            return r * (r + 1) // 2 - (l - 1) * (l) // 2

        l = max(l, i - k + 1)
        r = min(r, i + k - 1)

        # linear piece
        seg2_start = max(l, r - k + 1)
        l_start_val = min(r, l + k - 1) - i + 1
        l_end_val = l_start_val + (seg2_start - l) - 1
        seg1_total = range_sum(l_start_val, l_end_val)

        # constant piece
        seg2_width = r - i + 1
        seg2_height = i - seg2_start + 1
        seg2_total = seg2_height * seg2_width

        return seg1_total + seg2_total

    total = 0
    for i in range(n):
        # subarrays with nums[i] as smallest
        l = prev_smaller[i] + 1
        r = nxt_smaller[i] - 1
        total += count_subarrays(l, r, i) * nums[i]

        l = prev_larger[i] + 1
        r = nxt_larger[i] - 1
        total += count_subarrays(l, r, i) * nums[i]

    return total


print(minMaxSubarraySum([6, 17, 1], 3))  # 107
print(minMaxSubarraySum(nums=[1, 2, 3], k=2))  # 20
print(minMaxSubarraySum(nums=[1, -3, 1], k=2))  # -6
