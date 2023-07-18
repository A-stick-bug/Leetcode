def climbStairs(self, n: int) -> int:
    a = b = 1

    for i in range(n):
        temp = a + b
        a = b
        b = temp

    return a
