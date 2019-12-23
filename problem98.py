# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTWithRange(root, -9999999, 32147483647)

    def isValidBSTWithRange(self, node: TreeNode, min_range: int, max_range: int) -> bool:
        if node == None:
            return True
        elif min_range <= node.val <= max_range:
            return self.isValidBSTWithRange(node.left, min_range, node.val) and self.isValidBSTWithRange(node.right, node.val, max_range)
        else:
            return False
