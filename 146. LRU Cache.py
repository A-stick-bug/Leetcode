# https://leetcode.com/problems/lru-cache
# Doubly linked list, here we make it implicit to save memory
# The linked list is in order of usage, first element is LRU, last one is most recently used

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.get_idx = {}  # key: index
        self.get_key = {}  # reverse mapping, index : key
        self.cache = {}

        # represents doubly linked list, 0 and -1 are endpoints
        self.prev = [0] * (self.cap + 2)
        self.nxt = [-1] * (self.cap + 2)
        self.size = 0

    def _remove_node(self, cur):  # removes a node from the linked list
        prev = self.prev[cur]
        nxt = self.nxt[cur]
        self.nxt[prev] = nxt
        self.prev[nxt] = prev

    def _append_node(self, cur):  # adds a node to the end of the linked list
        last = self.prev[-1]

        self.nxt[last] = cur
        self.nxt[cur] = -1
        self.prev[cur] = last
        self.prev[-1] = cur

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        cur = self.get_idx[key]  # most recently used, move to end
        self._remove_node(cur)
        self._append_node(cur)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # already exists
            self.cache[key] = value
            cur = self.get_idx[key]
            self._remove_node(cur)  # update usage
            self._append_node(cur)
            return

        self.cache[key] = value
        if self.size == self.cap:  # full
            to_rem = self.nxt[0]
            k = self.get_key[to_rem]
            del self.cache[k]
            del self.get_idx[k]

            cur = self.nxt[0]
            self._remove_node(self.nxt[0])  # remove LRU (first node)

        else:
            self.size += 1
            cur = self.size

        self.get_idx[key] = cur
        self.get_key[cur] = key

        self._append_node(cur)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    lc = LRUCache(2)
    lc.put(1, 1)  # cache is {1=1}
    lc.put(2, 2)  # cache is {1=1, 2=2}
    print(lc.get(1))  # return 1
    lc.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lc.get(2))  # returns -1 (not found)
    lc.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lc.get(1))  # return -1 (not found)
    print(lc.get(3))  # return 3
    print(lc.get(4))  # return 4
