from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        min_num = min(nums)
        max_num = max(nums)

        if max_num - min_num == len(nums) - 1:
            return max_num + 1 if min_num == 0 else min_num - 1
        else:
            return (int)((max_num + min_num) * (len(nums) + 1) / 2 - s)
