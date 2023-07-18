def dailyTemperatures(temperatures):
    stack = []  # monotonic stack, decreasing order
    res = [0]*len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res


print(dailyTemperatures([73,74,75,71,69,72,76,73]))
