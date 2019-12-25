# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        nodes = []
        nodes.append(root)
        while len(nodes) != 0:
            res.append(nodes[-1].val)
            length = len(nodes)
            for i in range(length):
                node = nodes[i]
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            for i in range(length):
                del nodes[0]
        return res