# 'pad' array with 0s in front and end to prevent index out of range

def canPlaceFlowers(flowerbed,n):
    if n == 0:
        return True
    i = 0
    count = 0
    length = len(flowerbed)

    while count < n and i < length:
        if (flowerbed[i] == 0) and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
        i += 1

    return n == count


flower = [1,0,0,0,1,0,0]
print(canPlaceFlowers(flower,2))