from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        prev = 0
        while i < len(nums):
            if i == 0:
                nums[j] = nums[i]
                prev = nums[i]
            else:
                if nums[i] != prev:
                    prev = nums[i]
                    nums[j] = nums[i]
                    j += 1
                i += 1
        return j