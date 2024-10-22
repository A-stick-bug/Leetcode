"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree
For each node, store the value and the children structure
"""


class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "X"
        childs = []  # 0: leaf node, 1: left child, 2: right child, 3: both childs
        values = []  # value of node i

        def dfs(cur):
            childs.append((cur.left != None) + 2 * (cur.right != None))
            values.append(cur.val)
            if cur.left != None:
                dfs(cur.left)
            if cur.right != None:
                dfs(cur.right)

        dfs(root)
        return ",".join(map(str, childs)) + "/" + ",".join(map(str, values))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "X":
            return None
        childs, values = data.split("/")
        childs = list(map(int, childs.split(",")))
        values = list(map(int, values.split(",")))

        root = TreeNode()
        idx = 0

        def build(cur):
            nonlocal idx
            cur.val = values[idx]
            cc = childs[idx]

            if cc == 0:  # leaf
                return
            if cc == 1 or cc == 3:
                idx += 1
                cur.left = TreeNode()
                build(cur.left)
            if cc == 2 or cc == 3:
                idx += 1
                cur.right = TreeNode()
                build(cur.right)

        build(root)
        return root
