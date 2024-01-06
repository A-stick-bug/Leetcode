# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
# pretty much a template LIS

from bisect import bisect_right

def longestObstacleCourseAtEachPosition(obstacles: list[int]) -> list[int]:
    lis = []
    res = []
    for n in obstacles:
        i = bisect_right(lis, n)
        res.append(i+1)
        if i == len(lis):  # current element is largest
            lis.append(n)
        else:
            lis[i] = n

    return res


print(longestObstacleCourseAtEachPosition(obstacles = [2,2,1]))
