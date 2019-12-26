class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        diff = []
        has_dup = False
        charset = set()
        for i in range(len(A)):
            if A[i] not in charset:
                charset.add(A[i])
            elif A[i] in charset:
                has_dup = True
            if A[i] != B[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
        if len(diff) == 0 and has_dup:
            return True
        if len(diff) != 2:
            return False
        return A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]
