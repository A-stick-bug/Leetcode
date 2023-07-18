def addDigits(num):
    while num > 9:
        digit_total = 0
        temp = num
        # find sum of digits
        while temp > 0:
            digit_total += temp % 10
            temp //= 10
        num = digit_total
    return num


def nerdy_math_solution(num):
    return 1 + (num - 1) % 9 if num else 0

print(addDigits(38))
