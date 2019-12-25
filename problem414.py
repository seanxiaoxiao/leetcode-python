from typing import List

import sys

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        min = -sys.maxsize -1
        first_maximum = min
        second_maximum = min
        third_maximum = min
        for num in nums:
            if num > first_maximum:
                third_maximum = second_maximum
                second_maximum = first_maximum
                first_maximum = num
            elif num > second_maximum and num < first_maximum:
                third_maximum = second_maximum
                second_maximum = num
            elif num > third_maximum and num < second_maximum:
                third_maximum = num

        if third_maximum != min:
            return third_maximum
        else:
            return first_maximum

s = Solution()
print(s.thirdMax([2,3,1]))