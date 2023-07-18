def distanceTraveled(mainTank: int, additionalTank: int) -> int:
    miles = 1
    while mainTank > 0:
        if miles % 5 == 0 and additionalTank > 0:
            additionalTank -= 1
            mainTank += 1
        mainTank -= 1
        miles += 1
    return miles*10 - 10


print(distanceTraveled(1,2))
