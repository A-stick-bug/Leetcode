# Check out [LC 208. Implement Trie] first if you haven't

from collections import defaultdict


class Trie:
    def __init__(self):
        self.count = 0  # number of times this word is stored
        self.prefix_count = 0  # number of words that can be reached from this node
        self.children = defaultdict(Trie)

    def insert(self, word: str) -> None:
        """
        - The prefix_count of each node is how many words you can reach from this node
        - Update this every time a word is added, so we don't have to run a BFS for the countWordsStartingWith function
        """
        cur = self
        for char in word:
            cur = cur.children[char]
            cur.prefix_count += 1
        cur.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        """Count how many times the word appears in the trie, we just use the count value at the end of the word"""
        cur = self
        for char in word:
            if char not in cur.children:  # word is not it trie
                return 0
            cur = cur.children[char]
        return cur.count  # return the number of time the word appears

    def countWordsStartingWith(self, prefix: str) -> int:
        """
        Count the number of words with a certain prefix, we can just use the value at the node of the end of the prefix
        That value is updated every time a new word is added
        """
        cur = self
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.prefix_count

    def erase(self, word: str) -> None:
        """
        Delete 1 occurrence of the word from the trie, we have to update the prefix_count of every letter
        and the count of the word
        Note: we delete the actual nodes from the trie to save time when searching for a word
        """
        cur = self
        for char in word:
            next_char = cur.children[char]
            next_char.prefix_count -= 1
            if next_char.prefix_count == 0:
                cur.children.pop(char)
            cur = next_char
        cur.count -= 1
