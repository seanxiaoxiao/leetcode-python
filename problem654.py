# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

import heapq

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        index_map = {}
        heap = []
        for i in range(len(nums)):
            index_map[nums[i]] = i
            heapq.heappush(heap, -nums[i])

        if len(nums) == 0:
            return None
        root_val = -heapq.heappop(heap)
        root_index_val =  index_map[root_val]

        root = TreeNode(root_val)
        root_index = TreeNode(root_index_val)

        while len(heap) != 0:
            node_val = -heapq.heappop(heap)
            node_index = index_map[node_val]
            tree_node = root
            index_node = root_index
            parent_node = None
            parent_index_node = None
            while tree_node:
                parent_node = tree_node
                parent_index_node = index_node
                if node_index > index_node.val:
                    tree_node = tree_node.right
                    index_node = index_node.right
                else:
                    tree_node = tree_node.left
                    index_node = index_node.left
            if node_index > parent_index_node.val:
                parent_node.right = TreeNode(node_val)
                parent_index_node.right = TreeNode(node_index)
            else:
                parent_node.left = TreeNode(node_val)
                parent_index_node.left = TreeNode(node_index)
        return root

s = Solution()
s.constructMaximumBinaryTree([3,2,1,6,0,5])