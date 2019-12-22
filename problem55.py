from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_jumps = [None] * len(nums)
        self.doJump(0, nums, can_jumps)
        return can_jumps[len(nums) - 1]

    def doJump(self, index: int, nums: List[int], can_jumps: List[bool]):
        if index >= len(nums):
            return False
        elif index == len(nums) - 1:
            can_jumps[len(nums) - 1] = True
            return True
        elif can_jumps[index] is not None:
            return can_jumps[index]
        steps = nums[index]
        can_jump = False
        for i in reversed(range(1, steps + 1)):
            can_jump = can_jump or self.doJump(index + i, nums, can_jumps)
        can_jumps[index] = can_jump
        return can_jump

s = Solution()
print(s.canJump([2,3,1,1,4]))