# using DFS and a 2D array to keep track of layers
# reverse the array when returning, as we are starting from the bottom

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        layers = []

        def dfs(node: TreeNode, layer: int):
            if node is None:
                return

            if len(layers) <= layer:  # add new layer
                layers.append([node.val])
            else:
                layers[layer].append(node.val)  # add to existing later

            dfs(node.left, layer + 1)
            dfs(node.right, layer + 1)

        dfs(root, 0)
        return layers[::-1]
