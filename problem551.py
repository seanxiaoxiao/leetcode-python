class Solution:
    def checkRecord(self, s: str) -> bool:
        A_num = 0
        L_num = 0
        for c in s:
            if c == 'A':
                A_num += 1
                L_num = 0
                if A_num > 1:
                    return False
            elif c == 'L':
                L_num += 1
                if A_num >= 3:
                    return False
            else:
                L_num = 0

        return True