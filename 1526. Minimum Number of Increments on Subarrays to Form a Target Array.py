# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
# Monotonic stack
# Intuition: the stack maintains all currently extending increments
# - When adding a new element that is less than something in the stack
#   we extend a previous increment
# - Higher elements are cut off by the current one

def minNumberOperations(target: list[int]) -> int:
    stack = [0]  # placeholder to prevent index errors
    total = 0

    for cur in target:
        # try extending a previous subarray
        if stack[-1] > cur:
            while stack[-1] >= cur:
                stack.pop()
            stack.append(cur)

        else:  # add new subarray
            total += cur - stack[-1]
            stack.append(cur)

    return total

