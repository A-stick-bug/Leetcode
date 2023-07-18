from collections import deque


def ladderLength(beginWord, endWord, wordList):
    graph = {word:[] for word in wordList}
    graph[beginWord] = []
    for i in wordList:
        if compare(i,beginWord):
            graph[beginWord].append(i)

    for i in wordList:
        for j in wordList:
            if compare(i,j):
                graph[i].append(j)

    return bfs(graph,beginWord,endWord)

def compare(first,second):
    dif = 0
    i = 0
    while i < len(first) and dif <= 1:
        if first[i] != second[i]:
            dif += 1
        i += 1
    return dif == 1


def bfs(graph, start, end):
    queue = deque([start])
    visited = set()
    distance = {start: 0}

    while queue:
        node = queue.popleft()
        if node == end:
            return distance[node]

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                if neighbor in distance.keys():
                    distance[neighbor] = min(distance[node] + 1, distance[neighbor])
                else:
                    distance[neighbor] = distance[node] + 1
    return 0


beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log"]
print(ladderLength(beginWord,endWord,wordList))
