class Solution:
    nums = [None] * 38

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif self.nums[n] is not None:
            return self.nums[n]
        else:
            res = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            self.nums[n] = res
            return res
