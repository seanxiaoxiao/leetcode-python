# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        return self.doBuildTree(preorder, inorder)

    def doBuildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        node_val = preorder[0]
        node = TreeNode(node_val)
        inorder_index = inorder.index(node_val)
        preorder_left = preorder[1: inorder_index + 1]
        inorder_left = inorder[0: inorder_index]
        node.left = self.doBuildTree(preorder_left, inorder_left)
        preorder_right = preorder[inorder_index + 1:]
        inorder_right = inorder[inorder_index + 1:]
        node.right = self.doBuildTree(preorder_right, inorder_right)
        return node
