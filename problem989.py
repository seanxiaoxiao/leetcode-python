from typing import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        i = len(A) - 1
        while i >= 0 and K != 0:
            num1 = int(K % 10)
            num2 = A[i]
            A[i] = int((carry + num1 + num2) % 10)
            carry = int((carry + num1 + num2) / 10)
            K = int(K / 10)
            i -= 1

        addition = []
        while K != 0:
            num = int(K % 10)
            addition.insert(0, int((carry + num % 10)))
            carry = int((carry + num) / 10)
            K = int(K / 10)

        while i >= 0:
            num = A[i]
            A[i] = int((carry + num % 10))
            carry = int((carry + num) / 10)
            i -= 1

        if carry == 1:
            addition.insert(0, 1)

        addition.extend(A)
        return addition