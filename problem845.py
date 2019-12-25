from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        is_ascending = False
        is_descending = False
        length = 0
        res = 0
        i = 0
        while i < len(A):
            if not is_ascending and i < len(A) - 1:
                if A[i] < A[i + 1]:
                    is_ascending = True
                    is_descending = False
                    length = 1
                    i += 1
                else:
                    i += 1
            elif is_ascending == True and is_descending == False:
                if A[i] > A[i - 1]:
                    length += 1
                    i += 1
                elif A[i] < A[i - 1]:
                    is_descending = True
                    length += 1
                    i += 1
                else:
                    is_ascending = False
                    is_descending = False
            elif is_descending == True:
                if A[i] < A[i - 1]:
                    i += 1
                    length += 1
                else:
                    is_ascending = False
                    is_descending = False
                    res = max(res, length)
                    i -= 1
            else:
                i += 1
        if is_descending:
            res = max(res, length)
        return res

s = Solution()
print(s.longestMountain([2,3,3,2,0,2]))