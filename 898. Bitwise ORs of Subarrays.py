# https://leetcode.com/problems/bitwise-ors-of-subarrays
# Similar to subarray DP
# Key observation: there are at most N * log(10^9) subarray ORs
# Consider starting at each index i and extending left, each time you get a new value, you must set at least 1 bit
# You can set at most log(10^9) bits before every bit is set (no more new values)

def subarrayBitwiseORs(arr: list[int]) -> int:
    n = len(arr)

    res = set()
    cur = set()
    for i in range(n):
        cur = {x | arr[i] for x in cur}  # extend previous
        cur.add(arr[i])  # new start
        res.update(cur)
    return len(res)


print(subarrayBitwiseORs([1, 1, 2]))
