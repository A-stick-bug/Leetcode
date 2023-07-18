from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        queue=deque([node])
        copy ={node.val: Node(node.val, [])}

        while queue:
            current_node = queue.popleft()
            temp = copy[current_node.val]
            for n in current_node.neighbors:
                if n.val not in copy:
                    copy[n.val] = Node(n.val, [])
                    queue.append(n)
                temp.neighbors.append(copy[n.val])
        return copy[node.val]
