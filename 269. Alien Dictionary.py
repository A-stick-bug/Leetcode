"""
https://leetcode.com/problems/alien-dictionary/
Harder topological sort problem, this one requires some thinking

Based on the dictionary we are given, we can determine whether a letter comes before another,
creating a graph. Doing this in O(n*s) is the hard part (n is number of words, s is letter per word)

Key observation:
When creating the graph, we only need to compare the letters of adjacent words instead of all pairs
of words. This reduces the time complexity O(s*n^2) -> O(s*n)

Then, we can use Khan's algorithm for topological sort to get the alphabet
Note: we can output any valid solution so if there is many things in the queue (>1 possibility), we just take any
"""

from collections import defaultdict, deque


def alienOrder(words: list[str]) -> str:
    all_letters = set("".join(words))
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]  # compare adjacent words

        # corner case: a word that is the prefix of a shorter word, it must come after the shorter word
        if len(word1) != len(word2) and word1.startswith(word2):
            return ""

        for char1, char2 in zip(word1, word2):  # zip automatically crops out the extra letters in the longer word
            if char1 != char2:  # ignore same leading characters as they don't tell us anything about the order
                graph[char1].append(char2)  # char1 is before char2
                in_degree[char2] += 1
                break

    # topological sort
    order = []
    q = deque(i for i in all_letters if in_degree[i] == 0)
    while q:
        cur = q.popleft()
        order.append(cur)
        for next_letter in graph[cur]:
            in_degree[next_letter] -= 1
            if in_degree[next_letter] == 0:
                q.append(next_letter)

    if len(order) == len(all_letters):
        return "".join(order)
    else:
        return ""


print(alienOrder(["z", "z"]))
