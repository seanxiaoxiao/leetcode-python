class Solution:
    def dayOfYear(self, date: str) -> int:
        days_array = [31,28,31,30,31,30,31,31,30,31,30,31]
        components = date.split("-")
        year = int(components[0])
        is_leap_year = self.isLeapYear(year)
        month = int(components[1])
        day = int(components[2])
        if month  - 1 >= 0:
            days = day
            for i in range(month - 1):
                days += days_array[i]
            if month >= 3 and is_leap_year:
                days += 1
            return days
        else:
            return day


    def isLeapYear(self, year) -> bool:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

s = Solution()
print(s.dayOfYear("2004-03-01"))
print(s.dayOfYear("2003-03-01"))
print(s.dayOfYear("2019-02-10"))
print(s.dayOfYear("2019-01-09"))