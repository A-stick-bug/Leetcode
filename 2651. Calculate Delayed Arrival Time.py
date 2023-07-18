def findDelayedArrivalTime(arrivalTime, delayedTime):
    total_time = arrivalTime + delayedTime
    if total_time >= 24:
        total_time %= 24
    return total_time

print(findDelayedArrivalTime(9,11))