from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [None] * len(cost)
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2, len(cost)):
            self.calculateCost(cost, res, i)
        return min(res[-1], res[-2])

    def calculateCost(self, cost: List[int], res: List[int], i: int):
        res[i] = min(res[i - 1], res[i - 2]) + cost[i]

s = Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
