# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys

class Solution:
    res = sys.maxsize
    node = None

    def closestValue(self, root: TreeNode, target: float) -> int:
        self.doEval(root, target)
        return self.node

    def doEval(self, node: TreeNode, target: float):
        if not node:
            return
        else:
            diff = abs(node.val - float)
            if diff < self.res:
                self.node == node
                self.res = diff
            self.doEval(node.left, target)
            self.doEval(node.right, target)