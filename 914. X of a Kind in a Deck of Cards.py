# use GCD
from collections import Counter
from math import gcd


def hasGroupsSizeX(deck):
    values = list(Counter(deck).values())

deck = [1,1,1,2,2,2,3,3]
print(hasGroupsSizeX(deck))
