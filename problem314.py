import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    left_level = 0
    right_level = -1

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return

        self.update_level(root, 0)
        res = []
        for i in range (self.right_level - self.left_level + 1):
            res.append([])
        queue = [(root, 0)]
        while len(queue) > 0:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue[0][0]
                level = queue[0][1]
                res[level - self.left_level].append(node.val)
                queue.pop(0)

                if node.left:
                    queue.append((node.left, level - 1))
                if node.right:
                    queue.append((node.right, level + 1))

        return res

    def update_level(self, node, level):
        if not node:
            return
        else:
            self.left_level = min(self.left_level, level)
            self.right_level = max(self.right_level, level)
        self.update_level(node.left, level - 1)
        self.update_level(node.right, level + 1)

