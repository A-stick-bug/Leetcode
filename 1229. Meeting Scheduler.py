from typing import List


def minAvailableDuration(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    slots1.sort()  # sort based on time slot start time
    slots2.sort()

    i = j = 0  # set up 2 pointers
    while i < len(slots1) and j < len(slots2):
        # the overlap between 2 times is min(end1, end2) - max(start1, start2)
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])
        overlap = end - start + 1

        if overlap > duration:  # found available time slot
            return [start, start + duration]

        if slots1[i][1] > slots2[j][1]:  # slot2 ends too early, increment pointer
            j += 1
        else:
            i += 1

    return []


slots1 = [[10, 60]]
slots2 = [[12, 17], [21, 50]]
duration = 8
print(minAvailableDuration(slots1, slots2, duration))
