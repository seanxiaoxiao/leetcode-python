from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = None
        for i in range(len(nums)):
            num = nums[i]
            if current != num:
                current = num
                j = i + 1
                k = len(nums) - 1
                target = -num
                while j < k:
                    if nums[j] + nums[k] == target:
                        record = []
                        record.append(nums[i])
                        record.append(nums[j])
                        record.append(nums[k])
                        res.append(record)
                        current_j = nums[j]
                        current_k = nums[k]
                        while j + 1 < len(nums) and current_j == nums[j + 1]:
                            j += 1
                        while k - 1 >= 0 and current_k == nums[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        j += 1
        return res
