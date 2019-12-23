from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        low_digit, low_significant = self.digitsAndSignificant(low)
        high_digit, high_significant = self.digitsAndSignificant(high)
        for i in range(low_digit, high_digit + 1):
            for j in range(1, 10):
                num = self.generateNumber(j, i)
                if num > high:
                    break
                if low <= num <= high:
                    result.append(num)
        return result

    def generateNumber(self, siginificant, n):
        if siginificant + n > 10:
            return 0
        res = 0
        for i in range(siginificant, siginificant + n):
            res = res * 10
            res += i
        return res


    def digitsAndSignificant(self, num):
        digit = 0
        significant= 0
        while num != 0:
            significant = num % 10
            num = (int)(num / 10)
            digit += 1
        return (digit, significant)

s = Solution()
print(s.sequentialDigits(100, 300))