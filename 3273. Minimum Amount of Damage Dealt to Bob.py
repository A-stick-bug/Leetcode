# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob
# - first realize that only greedy is possible due to constraints
# - we don't care how much HP a monster has, only now many hits it takes to kill
# - if we deal damage to a monster, always finish it off before the next one
# - greedy sorting by damage/health ratio, biggest first

def minDamage(power: int, damage: list[int], health: list[int]) -> int:
    health = list(map(lambda x: (x + power - 1) // power, health))  # number of hits to kill
    monster = list(zip(damage, health))
    monster.sort(key=lambda x: x[0] / x[1], reverse=True)

    move = 0
    total = 0
    for d, h in monster:
        move += h
        total += d * move
    return total


print(minDamage(power=1, damage=[1, 2], health=[2, 1]))
print(minDamage(power=4, damage=[1, 2, 3, 4], health=[4, 5, 6, 8]))
