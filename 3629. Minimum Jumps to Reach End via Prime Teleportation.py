# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation
# Reverse the graph
# BFS states: [whether we can do teleportation on next move][index]
#
# Claim: You never do 2 teleportations in a row
#
# TC: O(sieve + n*log(MAX=1e6))

from collections import defaultdict, deque
from typing import List

MN = 10 ** 6 + 1
prime = [[] for _ in range(MN)]
for i in range(2, MN):
    if not prime[i]:
        for j in range(i + i, MN, i):
            prime[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        n = len(nums)
        loc = defaultdict(list)
        for i in range(n):
            loc[nums[i]].append(i)

        dist = [[-1] * n for _ in range(2)]
        dist[1][-1] = 0
        q = deque([(n - 1, True)])
        while q:
            cur, jump = q.popleft()
            if cur == 0:
                return dist[jump][cur]

            adjs = []
            if cur != 0:
                adjs.append((cur - 1, True))
            if cur != n - 1:
                adjs.append((cur + 1, True))

            if nums[cur] != 1 and len(prime[nums[cur]]) == 0:  # prime
                if jump:  # other same
                    adjs.extend([(i, False) for i in loc[nums[cur]] if i != cur])
            else:
                for p in prime[nums[cur]]:
                    adjs.extend([(i, False) for i in loc[p]])

            for adj, j in adjs:
                if 0 <= adj < n and dist[j][adj] == -1:
                    dist[j][adj] = dist[jump][cur] + 1
                    q.append((adj, j))
