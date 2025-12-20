# https://leetcode.com/problems/count-primes
# Significant speedups to sieve using numpy
# Note that we could also precompute the bool array and take the prefix sum

import numpy as np


def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    is_prime = np.full(n, True, dtype=bool)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i::i] = False
    return int(is_prime.sum())


print(countPrimes(10))
print(countPrimes(0))
