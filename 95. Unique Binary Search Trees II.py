# https://leetcode.com/problems/unique-binary-search-trees-ii/
# unlike the version of this question that only asks for the NUMBER of BSTs
# DP doesn't help much here (around the same runtime), probably because n is so small

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(l, r):
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]

            res = []
            for i in range(l, r + 1):
                left = solve(l, i - 1)
                right = solve(i + 1, r)

                # pair up every left and right
                for l_node in left:
                    for r_node in right:
                        res.append(TreeNode(i, l_node, r_node))
            return res

        return solve(1, n)


print(Solution().generateTrees(3))
