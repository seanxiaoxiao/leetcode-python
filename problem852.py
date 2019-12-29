from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        res = 0
        for i in range(1, len(A) - 1):
            if A[i] > A[i - 1] and A[i] > A[i + 1] and A[i] > res:
                res = i
        return res
