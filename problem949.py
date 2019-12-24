from typing import List

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        if A.count(2) > 0:
            nums = A[:]
            res = self.construct_with_twenty_hour(nums)
            if len(res) > 0:
                return res
            else:
                nums = A[:]
                return self.consturct_with_less_twenty_hour(nums)
        else:
            return self.consturct_with_less_twenty_hour(A)

    def construct_with_twenty_hour(self, A: List[int]) -> str:
        ten_hour = 2
        A.remove(ten_hour)

        hour = -1
        for num in A:
            if ten_hour == 2 and num <= 3 and num > hour:
                hour = num
            elif ten_hour != 2 and num > hour:
                hour = num
        if hour == -1:
            return ""
        else:
            A.remove(hour)

        ten_minute = -1
        for num in A:
            if num > ten_minute and num <= 5:
                ten_minute = num
        if ten_minute == -1:
            return ""
        else:
            A.remove(ten_minute)

        return str(ten_hour) + str(hour) + ":" + str(ten_minute) + str(A[0])

    def consturct_with_less_twenty_hour(self, A: List[int]) -> str:
        ten_hour = -1
        for num in A:
            if num > ten_hour and num <= 1:
                ten_hour = num
        if ten_hour != -1:
            A.remove(ten_hour)
        else:
            return ""

        hour = -1
        for num in A:
            if num > hour:
                hour = num
        if hour == -1:
            return ""
        else:
            A.remove(hour)

        ten_minute = -1
        for num in A:
            if num > ten_minute and num <= 5:
                ten_minute = num
        if ten_minute == -1:
            return ""
        else:
            A.remove(ten_minute)

        return str(ten_hour) + str(hour) + ":" + str(ten_minute) + str(A[0])

s = Solution()
s.largestTimeFromDigits([5,5,5,5])
