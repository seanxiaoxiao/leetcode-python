from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        res = [ [ 0 for i in range(col) ] for j in range(row) ]
        for i in range(row):
            for j in range(col):
                res[j][i] = A[i][j]
        return res