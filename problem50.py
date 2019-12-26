class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        else:
            return self.doPow(x, n)

    def doPow(self, x: float, n: int):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            num = self.doPow(x, int(n / 2))
            num = num * num
            if n % 2 == 1:
                num = num * x
            return num


s = Solution()
print(s.myPow(2, 5))