from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        num_map = {}
        sorted_num = []
        for num in nums:
            if not num_map.get(num):
                sorted_num.append(num)
                num_map[num] = 0
            num_map[num] += 1
        sorted_num.sort()
        while len(sorted_num) != 0:
            prev = None
            index_to_remove = []
            for i in range(k):
                current = sorted_num[i]
                if prev is not None and current - prev != 1:
                    return False
                else:
                    prev = current
                    num_map[current] -= 1
                    if num_map[current] == 0:
                        index_to_remove.append(i)
            offset = 0
            for i in index_to_remove:
                del sorted_num[i - offset]
                offset += 1
        return True

s = Solution()
print(s.isPossibleDivide([1,2,3,3,4,4,5,6], 4))