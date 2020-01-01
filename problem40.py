from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        temp = []
        self.doCombination(candidates, 0, target, res, temp)
        return res

    def doCombination(self, candidates, startIndex, remain, res, temp):
        if remain == 0:
            res.append(temp)
        else:
            nums = set()
            for i in range(startIndex, len(candidates)):
                if candidates[i] not in nums and remain - candidates[i] >= 0:
                    nums.add(candidates[i])
                    new_temp = temp[:]
                    new_temp.append(candidates[i])
                    self.doCombination(candidates, i + 1, remain - candidates[i], res, new_temp)
