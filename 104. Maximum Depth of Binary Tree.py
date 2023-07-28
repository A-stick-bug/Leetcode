# DFS solution

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0  # keep track of maximum depth

        def dfs(node: TreeNode, depth: int):
            nonlocal res

            if node is None:  # end of branch
                return
            dfs(node.right, depth + 1)  # continue down left and right
            dfs(node.left, depth + 1)
            res = max(res, depth)

        dfs(root, 1)  # depth of root is 1
        return res
