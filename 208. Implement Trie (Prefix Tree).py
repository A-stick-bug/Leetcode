class TrieNode:
    def __init__(self, end):
        self.children = {}
        self.end = end


class Trie:
    def __init__(self):
        self.root = TrieNode(False)

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(False)
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # return True
trie.search("app")  # return False
trie.startsWith("app")  # return True
trie.insert("app")
trie.search("app")  # True
