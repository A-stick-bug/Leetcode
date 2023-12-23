# template topological sort question (we can use Khan's algorithm)

from collections import deque


def canFinish(numCourses, prerequisites):
    after = [[] for _ in range(numCourses)]
    in_degree = [0]*numCourses
    for course, req in prerequisites:
        after[req].append(course)
        in_degree[course] += 1

    q = deque(i for i in range(numCourses) if in_degree[i] == 0)
    while q:
        cur = q.popleft()
        for adj in after[cur]:
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                q.append(adj)

    return sum(in_degree) == 0


print(canFinish(2,[[0,1]]))