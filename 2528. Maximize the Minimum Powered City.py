# https://leetcode.com/problems/maximize-the-minimum-powered-city/description/
# When the question asks to minimize/maximize something, first consider binary search
#
# First we use a difference array + PSA to get how much power each city gets
# Then, we binary search for the max-min power of a city

from itertools import accumulate


def maxPower(stations: list[int], r: int, k: int) -> int:
    n = len(stations)
    diff = [0] * (n + 1)

    for i, cnt in enumerate(stations):  # create difference array
        diff[max(0, i - r)] += cnt
        diff[min(n - 1, i + r) + 1] -= cnt
    arr = list(accumulate(diff))[:-1]  # turn back into regular array using PSA, city i has arr[i] stations powering it
    width = r * 2 + 1  # putting a power station creates power for this many cities

    def works(m):
        """check if it is possible for the least powered city to have a power of at least m"""
        state = arr.copy()
        diff = [0] * (n + 1)
        rem = k  # number of power stations we can build
        adding = 0

        for i in range(n):
            adding += diff[i]
            state[i] += adding
            if state[i] < m:  # put extra power stations so the current one gets >= m
                need = m - state[i]
                if need > rem:  # out of stations to place
                    return False
                rem -= need

                # after putting power stations optimally, it will also power the next WIDTH houses
                diff[min(n, i + width)] -= need
                adding += need
        return True

    # template binary search
    low = 0
    high = 10 ** 14
    while low <= high:
        mid = (low + high) // 2
        if works(mid):
            low = mid + 1
        else:
            high = mid - 1

    return low - 1


print(maxPower(stations=[1, 2, 4, 5, 0], r=1, k=2))
