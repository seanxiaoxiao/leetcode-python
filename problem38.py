class Solution:
    def nextNum(self, current_num):
        result = ""
        current_digit = ""
        count = 0
        for num in current_num:
            if current_digit != num:
                if count != 0:
                    result = result + str(count) + current_digit
                current_digit = num
                count = 1
            else:
                count += 1
        if count != 0:
            result = result + str(count) + current_digit
                
        return result

    def countAndSay(self, n):
        result = "1"
        for i in range(0, n - 1):
            result = self.nextNum(result)
            print(result)
        return result