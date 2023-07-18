from collections import deque

def stringShift(s, shift) -> str:
    total = 0
    for direction, val in shift:
        if direction == 1:
            total -= val
        else:
            total += val
    s = deque(s)
    if total < 0:
        for i in range(-total):
            s.extendleft(s.pop())
    else:
        for i in range(total):
            s.append(s.popleft())
    return "".join(s)


def simpler_solution(s, shift) -> str:
    total = 0
    for direction, val in shift:
        if direction == 1:
            total -= val
        else:
            total += val
    total %= len(s)
    return s[-total:] + s[:-total]


print(stringShift("abc", [[0,1],[1,2]]))

