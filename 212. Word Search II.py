from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

    def insert(self, word):
        cur = self
        for letter in word:
            cur = cur.children[letter]  # defaultdict will create empty node if needed

        cur.word = word  # end node contains the word


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    n, m = len(board), len(board[0])
    dir_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    trie = TrieNode()
    res = []  # list of found words

    for word in words:
        trie.insert(word)

    def dfs(row, col, cur):
        # cur represents the TrieNode for the current cell
        if cur.word:
            res.append(cur.word)  # found a word
            cur.word = None  # mark as found to prevent duplicates

        # mark as visited, store value for later
        temp = board[row][col]
        board[row][col] = "#"

        # try adjacent cells
        for dr, dc in dir_4:
            new_r = row + dr
            new_c = col + dc

            # stay inside the board to prevent index out of range
            if 0 <= new_r < n and 0 <= new_c < m:
                adj = board[new_r][new_c]
                if adj in cur.children:
                    dfs(new_r, new_c, cur.children[adj])

        board[row][col] = temp  # backtrack

    # start a dfs from all cells where the first letter matches a word
    for i in range(n):
        for j in range(m):
            cell = board[i][j]
            if cell[0] in trie.children:
                dfs(i, j, trie.children[cell])

    return res


print(findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                words=["oath", "pea", "eat", "rain"]))
