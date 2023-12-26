# https://leetcode.com/problems/course-schedule-iii/description/
# greedy algorithm with max heap
# for each course, we check how many courses we can take in total if we take the current and possible ones before it

from heapq import heappop, heappush


def scheduleCourse(courses: list[list[int]]) -> int:
    courses.sort(key=lambda x: x[1])  # sort by end
    time = 0
    take = []  # max heap, make values negative
    res = 0

    for t, end in courses:
        heappush(take, -t)  # try to take current course
        time += t

        # we need to not take some previous courses in order to take the current course
        # we can greedily decide what courses not to take (the longest ones)
        while take and time > end:
            time -= -heappop(take)
        res = max(res, len(take))

    return res


print(scheduleCourse(courses=[[5, 5], [4, 6], [2, 6]]))


# TLE, O(NM), where N is the number of courses and M is the highest deadline date
# use knapsack DP, for each course, either take or don't take
def scheduleCourse_knapsack(courses: list[list[int]]) -> int:
    courses.sort(key=lambda x: x[1])  # sort by end
    days = max(courses, key=lambda x: x[1])[1]  # highest time

    dp = [0] * (days + 1)
    for time, deadline in courses:
        for i in reversed(range(time, deadline + 1)):
            dp[i] = max(dp[i], dp[i - time] + 1)
    return max(dp)
