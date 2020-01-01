from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        count = 0
        index = 0
        i = 0
        while i < len(chars):
            current = chars[i]
            if prev == current:
                count += 1
            else:
                chars[index] = prev
                index += 1
                if count != 1:
                    count_str = str(count)
                    for j in range(len(count_str)):
                        chars[index] = count_str[j]
                        index += 1
                prev = current
                count = 1
            i += 1
        chars[index] = prev
        index += 1
        if count != 1:
            count_str = str(count)
            for j in range(len(count_str)):
                chars[index] = count_str[j]
                index += 1
        return index

s = Solution()
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))