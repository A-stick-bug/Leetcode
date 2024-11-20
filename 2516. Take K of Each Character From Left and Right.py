# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right
# optimizing a stupid brute force with binary search and PSA
# note: sliding window solution is much better

from itertools import accumulate


def takeCharacters(s: str, k: int) -> int:
    if k == 0:
        return 0
    n = len(s)
    s = list(map(lambda x: ord(x) - ord("a"), s))

    freq = [[s[j] == i for j in range(n)] for i in range(3)]
    for i in range(3):
        freq[i] = [0] + list(accumulate(freq[i]))
    query = lambda val, l, r: freq[val][r + 1] - freq[val][l]

    def works(le):
        cnt = [query(val, n - le, n - 1) for val in range(3)]
        if all(i >= k for i in cnt):
            return True
        for i in range(le):
            cnt = [query(val, 0, i) + query(val, n - le + i + 1, n - 1) for val in range(3)]
            if all(i >= k for i in cnt):
                return True
        return False

    ans = -1
    low = 3 * k
    high = n
    while low <= high:
        mid = (low + high) // 2
        if works(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


print(takeCharacters(s="cbbac", k=1))
print(takeCharacters(s="a", k=0))
