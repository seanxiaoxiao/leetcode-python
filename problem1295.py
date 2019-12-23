from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if self.isEvenDigit(num):
                count += 1
        return count

    def isEvenDigit(self, num):
        if num == 0:
            return False
        if num < 0:
            return self.isEvenDigit(self, -num)
        digit = 0
        while num != 0:
            digit += 1
            num = (int)(num / 10)
        return digit % 2 == 0

s = Solution()
s.findNumbers([555,901,482,1771])