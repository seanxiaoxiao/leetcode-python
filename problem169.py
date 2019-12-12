from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        current = 0
        for num in nums:
            if count == 0:
                current = num
                res = num
            if num == current:
                count += 1
            else:
                count -= 1
        return res
