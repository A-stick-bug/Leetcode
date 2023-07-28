from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:  # found value or value is not present
            return root

        if root.val < val:  # value is greater so search right
            return self.searchBST(root.right, val)
        else:  # value is smaller so search left
            return self.searchBST(root.left, val)
