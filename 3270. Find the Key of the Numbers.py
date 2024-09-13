def generateKey(num1: int, num2: int, num3: int) -> int:
    num1 = "0" * 4 + str(num1)
    num2 = "0" * 4 + str(num2)
    num3 = "0" * 4 + str(num3)

    return int(min(num1[-4], num2[-4], num3[-4]) +
               min(num1[-3], num2[-3], num3[-3]) +
               min(num1[-2], num2[-2], num3[-2]) +
               min(num1[-1], num2[-1], num3[-1]))
