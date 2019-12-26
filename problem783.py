# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys

class Solution:

    res = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        self.findMinForNode(root)
        return self.res

    def findMinForNode(self, node):
        if not node:
            return
        self.findMin(node)
        self.findMinForNode(node.left)
        self.findMinForNode(node.right)

    def findMin(self, node: TreeNode):
        if not node.left and not node.right:
            return
        if node.left:
            left = node.left
            prev = left
            while left:
                prev = left
                left = left.right
            self.res = min(self.res, node.val - prev.val)
        if node.right:
            right = node.right
            prev = right
            while right:
                prev = right
                right = node.left
            self.res = min(self.res, prev.val - node.val)

s = Solution()
root = TreeNode(4)
left = TreeNode(2)
right = TreeNode(6)
leftleft = TreeNode(1)
leftright = TreeNode(3)
root.left = left
root.right = right
left.left = leftleft
left.right = leftright
s.minDiffInBST(root)