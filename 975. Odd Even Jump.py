# https://leetcode.com/problems/odd-even-jump/
# Use DP to only compute the answer at each index once
# Use monotonic stack to get next greater and smaller element
# TC: O(nlogn) from sorting

def oddEvenJumps(arr: list[int]) -> int:
    n = len(arr)

    # compute next greater and next smaller indices using mono stack
    indices_sorted = sorted(range(n), key=lambda i: (arr[i], i))
    indices_rev = sorted(range(n), key=lambda i: (-arr[i], i))
    next_greater = [-1] * n
    next_smaller = [-1] * n
    stack1 = []
    stack2 = []
    for i, j in zip(indices_sorted, indices_rev):
        while stack1 and i >= stack1[-1]:
            next_greater[stack1.pop()] = i
        stack1.append(i)
        while stack2 and j >= stack2[-1]:
            next_smaller[stack2.pop()] = j
        stack2.append(j)

    good = [[-1] * n for _ in range(2)]
    good[0][-1] = good[1][-1] = 1  # base case: end is always good

    def solve(cur, parity):
        if cur == -1:
            return 0
        if good[parity][cur] != -1:
            return good[parity][cur]
        if parity == 1:  # odd
            good[parity][cur] = solve(next_greater[cur], parity ^ 1)
        else:  # even
            good[parity][cur] = solve(next_smaller[cur], parity ^ 1)
        return good[parity][cur]

    for i in range(n):
        solve(i, 1)
    # count valid indices at odd parity only since we start on odd
    return sum(i == 1 for i in good[1])


print(oddEvenJumps(arr=[5, 1, 3, 4, 2]))
