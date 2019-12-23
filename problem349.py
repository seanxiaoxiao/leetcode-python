from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        res = []
        for num in nums1:
            s1.add(num)
        for num in nums2:
            if num in s1 and num not in s2:
                res.append(num)
                s2.add(num)
        return res
