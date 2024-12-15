# https://leetcode.com/problems/digit-operations-to-make-two-integers-equal
# Dijkstra's algorithm on a custom graph
# note: apparently digits that become 0 don't count anymore...

from heapq import heappush, heappop

MN = 10 ** 5 + 1
is_prime = [True] * MN
is_prime[0] = is_prime[1] = False
for i in range(2, MN):
    if is_prime[i]:
        for j in range(i * i, MN, i):
            is_prime[j] = False


def minOperations(n: int, m: int) -> int:
    if is_prime[m] or is_prime[n]:
        return -1

    def get_adj(num):
        res = []
        for i in range(len(str(num))):
            d = int(str(num)[-i - 1])
            if d != 0:
                res.append(num - 10 ** i)
            if d != 9:
                res.append(num + 10 ** i)
        return res

    q = [(n, n)]
    vis = {n: n}
    while q:
        dist, cur = heappop(q)
        if cur == m:
            return dist

        for adj in get_adj(cur):
            if is_prime[adj] or (adj in vis and vis[adj] <= dist + adj):
                continue
            heappush(q, (dist + adj, adj))
            vis[adj] = dist + adj

    return -1


print(minOperations(10, 12))
print(minOperations(4, 8))
print(minOperations(6, 2))
print(minOperations(36, 50))
print(minOperations(5637, 2034))
