# https://leetcode.com/problems/house-robber-iii/description/
# Tree DP with memo because there are overlapping recursive calls

from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root) -> int:
    @cache
    def solve(node):
        if not node:  # empty subtree
            return 0

        take = 0
        if node.left:  # take current, skip next
            take += solve(node.left.left) + solve(node.left.right)
        if node.right:
            take += solve(node.right.right) + solve(node.right.left)

        # either take or don't take the current
        return max(node.val + take, solve(node.left) + solve(node.right))

    return solve(root, 0, 0)
