def sum_divisible_by_3_5_7(n):
    sum = 0

    for num in range(1, n+1):
        if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            print(num)
            sum += 1
    return sum


print(sum_divisible_by_3_5_7(105))