# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
# Divide by 2: remove trailing zero
# Add 1: add 1 to last digit and carry with addition
# amortized O(n)

def numSteps(s: str) -> int:
    s = [0] + list(map(int, s))  # padding
    n = len(s)
    total = 0
    i = n - 1
    while i > 0:
        if s[i] == 0:
            total += 1
            i -= 1
            continue
        else:
            t = i
            if i == 1 and s[1] == 1 and s[0] == 0:
                break
            while s[t] == 1:
                s[t] = 0
                t -= 1
            s[t] = 1
            total += 1
    return total


print(numSteps("11000"))
