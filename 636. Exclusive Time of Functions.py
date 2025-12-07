# https://leetcode.com/problems/exclusive-time-of-functions/description/
# stack, with careful interval tracking

def exclusiveTime(n: int, logs: list[str]) -> list[int]:
    stack = []
    prev = 0
    res = [0] * n

    for event in logs:
        num, type_, time = event.split(":")
        num, time = int(num), int(time)
        if type_ == "end":  # end interval
            time += 1

        if stack:
            res[stack[-1]] += time - prev

        if type_ == "start":
            stack.append(num)
        else:
            stack.pop()
        prev = time

    return res
