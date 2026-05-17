# https://leetcode.com/problems/design-add-and-search-words-data-structure
# Design choice: trade off memory and write speed for faster search speed
#
# - If we don't do this tradeoff, we will expand a wildcard 26x 1 more time during search
# - We can also take this tradeoff even further by considering both possible
#   wildcard positions but this is too memory intensive
#
# Analysis: let m = word length
# insert: O(m^2) per word insertion, costing O(m^2) memory
# search: O(26m) worst case due to single branching
#
# If we only store the word (without the first wildcard expansion), we get O(m) time and space for
# insert but O(26^2 * m) for search

class WordDictionary:
    def __init__(self):
        self.trie = {}  # ending key is `!`

    def _insert_to_trie(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["!"] = True

    def addWord(self, word: str) -> None:
        self._insert_to_trie(word)
        for i in range(len(word)):  # consider 1st wildcard at position i
            filled = word[:i] + "." + word[i + 1:]
            self._insert_to_trie(filled)

    def search(self, word: str) -> bool:
        n = len(word)
        wildcards = [i for i in range(n) if word[i] == "."]

        if len(wildcards) < 2:  # directly search
            cur = self.trie
            for c in word:
                if c not in cur:
                    return False
                cur = cur[c]
            return "!" in cur

        else:  # search up to second wildcard
            cur = self.trie
            for c in word[:wildcards[1]]:
                if c not in cur:
                    return False
                cur = cur[c]
            # expand to all characters (x26 in worst case)
            possible = list(cur.values())
            for cur in possible:  # try all possible
                works = True
                for c in word[wildcards[1] + 1:]:
                    if c not in cur:
                        works = False
                        break
                    cur = cur[c]
                if works and "!" in cur:
                    return True
            return False
