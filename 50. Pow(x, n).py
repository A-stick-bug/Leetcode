def myPow(x: float, n: int) -> float:
    if n < 0:
        n = abs(n)
        x = 1 / x

    temp = x
    for i in range(n - 1):
        x *= temp

    return x
