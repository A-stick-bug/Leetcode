from collections import deque


def canFinish(numCourses, prerequisites):
    graph = {}
    taken = set()
    for i in range(len(prerequisites)):  # creating the graph
        graph[prerequisites[i][0]] = prerequisites[i][1:]

    return numCourses == len(taken)


print(canFinish(2,[[1,0],[0,1]]))