# https://leetcode.com/problems/maximize-the-minimum-game-score
# Binary search and greedy to check if a value works
# - Bsearch on maximum possible minimum value
# - To check if a value works, check how many additions each index needs to reach that value
# - Greedy strategy: alternate indices i and i+1 until index i is cleared

def maxScore(points: list[int], m: int) -> int:
    n = len(points)

    def works(mi):
        # number of additions needed
        arr = [(mi + points[i] - 1) // points[i] for i in range(n)] + [0]
        moves = 0
        idx = -1
        for i in range(n):
            if arr[i] <= 0:
                continue
            moves += i - idx  # move from previous index to here
            arr[i] -= 1

            a, b = arr[i], arr[i + 1]

            if a >= b:
                arr[i + 1] = 0  # clearing i also clears i+1
                arr[i] = 0
                moves += 2 * a
            else:
                arr[i + 1] -= a  # clear i clears part of i+1
                arr[i] = 0
                moves += 2 * a
            idx = i

            if moves > m:
                return False
        if moves > m:
            return False
        return True

    low = 0
    high = 1 << 60
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if works(mid):
            best = max(best, mid)
            low = mid + 1
        else:
            high = mid - 1

    return best


print(maxScore([2, 4], m=3))
print(maxScore([12, 16, 19, 9], 7))  # 12
print(maxScore([9, 8], m=5))  # 16
print(maxScore(points=[2, 4], m=3))
print(maxScore(points=[1, 2, 3], m=5))
