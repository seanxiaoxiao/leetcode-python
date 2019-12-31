# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        result = []
        self.findNode(root, target, 0, K, result)
        return result

    def findNode(self, current: TreeNode, target: TreeNode, level: int, K: int, result):
        if not current:
            return None
        elif current == target:
            if K == 0:
                result.append(current.val)
            else:
                self.collectResult(K - 1, result, current.left)
                self.collectResult(K - 1, result, current.right)
            return level
        else:
            left_result =  self.findNode(current.left, target, level + 1, K, result)
            if left_result:
                diff = K - (left_result - level)
                if diff == 0:
                    result.append(current.val)
                else:
                    self.collectResult(diff - 1, result, current.right)
                return left_result
            else:
                right_result = self.findNode(current.right, target, level + 1, K, result)
                if right_result:
                    diff = K - (right_result - level)
                    if diff == 0:
                        result.append(current.val)
                    else:
                        self.collectResult(diff - 1, result, current.left)
                    return right_result

    def collectResult(self, level_remain, result, node: TreeNode):
        if not node:
            return
        elif level_remain == 0:
            result.append(node.val)
        else:
            self.collectResult(level_remain - 1, result, node.left)
            self.collectResult(level_remain - 1, result, node.right)
