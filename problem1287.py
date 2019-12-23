from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        gap = (int)(len(arr) / 4)
        for i in range(1, 4):
            candidate = arr[gap * i]
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate)
            if (right - left) * 4 > len(arr):
                return candidate
