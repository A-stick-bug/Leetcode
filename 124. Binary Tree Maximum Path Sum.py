"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

Tree DP question: store maximum possible inside a variable
O(n), where n is the number of nodes in the tree

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root) -> int:
    highest = -float('inf')

    def get_total(node: TreeNode | None):
        nonlocal highest
        if not node:
            return 0

        l = get_total(node.left)
        r = get_total(node.right)

        # if path goes through this node, it could also go through the left OR right node
        cur = max(node.val, node.val + l, node.val + r)

        # we could also have this node connect the left and right branches of the tree
        # if we do this, we cannot add any more nodes
        highest = max(highest, max(cur, node.val + l + r))

        return cur

    get_total(root)  # traverse tree to get maximum
    return highest
