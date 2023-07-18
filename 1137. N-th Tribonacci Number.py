# a = b, b = c != a = b = c

def tribonacci(n: int) -> int:
    a, b, c, temp = 0, 0, 1, 0
    for i in range(n + 1):
        temp = a + b + c
        a = b
        b = c
        c = temp

    return a

print(tribonacci(10))