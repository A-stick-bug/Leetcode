def smallestNumber(n: int) -> int:
    for i in range(1, 999999):
        if i.bit_count() == i.bit_length() and i >= n:
            return i
