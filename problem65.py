import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = m + n - 2
        return (int)(math.factorial(count) / math.factorial(m - 1) / math.factorial(n - 1))
