from typing import List

import sys

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = [None] * (len(nums) + 1)
        sums[0] = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sums[i + 1] = sum
        res = -sys.maxsize

        for j in range(len(nums) - k + 1):
            res = max(res, (sums[j + k] - sums[j]) / k)
        return res
