# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        else:
            val = postorder[-1]
            node = TreeNode(val)
            i = inorder.index(val)
            node.left = self.buildTree(inorder[0:i], postorder[0:i])
            node.right = self.buildTree(inorder[i+1:], postorder[i:-1])
            return node
