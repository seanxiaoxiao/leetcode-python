from typing import List

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        pre_max = 0
        for i in range(1, len(A)):
            pre_max = max(pre_max, A[i - 1] + i - 1)
            res = max(res, pre_max + A[i] - i)
        return res

s = Solution()
print(s.maxScoreSightseeingPair([8,1,5,2,6]))