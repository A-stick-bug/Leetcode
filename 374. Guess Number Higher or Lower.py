def guess(num):
    pass

def guessNumber(n: int) -> int:
    low = 1
    high = n
    while high >= low:
        mid = (high+low)//2
        if guess(mid) == -1:
            high = mid-1
        elif guess(mid) == 1:
            low = mid+1
        else:
            return mid