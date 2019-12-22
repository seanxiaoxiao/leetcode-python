from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.doCombine(res, [], 1, n, k)
        return res

    def doCombine(self, res: List[List[int]], current: List[int], num: int, n: int, k: int):
        if len(current) == k:
            res.append(current)
        elif num > n:
            return
        else:
            for i in range(num, n + 1):
                new_current = current[:]
                new_current.append(i)
                self.doCombine(res, new_current, i + 1, n, k)
