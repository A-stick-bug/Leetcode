import functools

def nth_fibonacci(n):
    # bottom-up dp, memory efficient
    a, b = 0, 1
    for i in range(n):
        temp = a + b
        a = b
        b = temp

    return a


def top_down_fibonacci(n):
    # top-down using memoization
    @functools.cache
    def fib(n):
        if n == 1 or n == 0:
            return 1
        return fib(n-1) + fib(n-2)

    return fib(n)


print(nth_fibonacci(8))