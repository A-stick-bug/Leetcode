def minimumMoves(s):
    count,i = 0,0
    while i < len(s):
        if s[i] == "X":
            count += 1
            i += 2
        i += 1
    return count


print(minimumMoves("OXXOX"))