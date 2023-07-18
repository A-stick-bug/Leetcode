# do more test cases before submitting

def countOdds(low: int, high: int) -> int:
    if (high - low + 1) % 2 == 0: # even number
        return (high - low + 1) // 2
    else: # odd number
        if high % 2 == 0 and low % 2 == 0:
            return (high - low + 1) // 2
        else:
            return ((high - low + 1) // 2) + 1



print(countOdds(8, 10))
