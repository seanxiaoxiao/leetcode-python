from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [None] * (n + 1)
        self.doClimb(n, steps)
        return steps[n]

    def doClimb(self, n: int, steps: List[int]):
        if n < 1:
            return 0
        elif n == 1:
            steps[1] = 1
            return 1
        elif n == 2:
            steps[2] = 2
            return 2
        elif steps[n] is not None:
            return steps[n]
        else:
            res = self.doClimb(n - 1, steps) + self.doClimb(n - 2, steps)
            steps[n] = res
            return res
