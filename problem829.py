class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        for i in range(1, N + 1):
            div = N / i
            if div - (i / 2) <= 0:
                break
            if i % 2 == 1 and N % i == 0:
                res += 1
            elif N % i == i  / 2:
                res += 1
        return res

s = Solution()
print(s.consecutiveNumbersSum(5))