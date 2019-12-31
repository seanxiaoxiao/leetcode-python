from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 0
        length = 0
        prev = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > prev:
                length += 1
            elif nums[i] <= prev:
                res = max(res, length)
                length = 1
            prev = nums[i]
        res = max(res, length)
        return res