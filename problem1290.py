# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        node = head
        while node != None:
            result *= 2
            result += node.val
            node = node.next
        return result
