def removeDigit(number,digit):
    biggest = 0
    for i,num in enumerate(number):
        if num == digit:
            biggest = max(biggest, int(number[:i]+number[i+1:]))

    return biggest

print(removeDigit("1231","1"))