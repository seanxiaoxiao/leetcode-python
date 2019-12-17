class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        current_num = 9
        swap_index = -1
        start_index = -1
        maximum = 0
        for i in range(len(num_str)):
            d = int(num_str[i])
            if d <= current_num:
                current_num = d
            else:
                if d >= maximum:
                    swap_index = i
                    maximum = d

        if swap_index != -1:
            for i in reversed(range(swap_index)):
                d = int(num_str[i])
                if d < maximum:
                    start_index = i
            return int(self.swap(num_str, start_index, swap_index))
        else:
            return num


    def swap(self, str, i, j):
        c = list(str)
        c[i], c[j] = c[j], c[i]
        return ''.join(c)



s = Solution()
print(s.maximumSwap(9937))