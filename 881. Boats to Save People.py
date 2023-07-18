"""
2023/4/3 daily leetcode
- Greedy algorithm with sorting and two pointers
Sorting is very important because you don't have to look for the heaviest+lightest pair
You can just take the first and last index and if the heaviest person can't go with a lighter person, give them a boat for themselves
"""

def numRescueBoats(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    num_boats = 0
    while left <= right:
        # heaviest and lightest person fit in a boat
        if people[left] + people[right] <= limit:
            left += 1
        # only heaviest person fits
        right -= 1
        num_boats += 1
    return num_boats


people = [3, 2, 2, 1]
print(numRescueBoats(people, 3))
