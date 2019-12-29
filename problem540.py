from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = int(i + (j - i) / 2)
            if mid == 0:
                if len(nums) == 1:
                    return nums[0]
                elif nums[mid] != nums[mid + 1]:
                    return nums[mid]
            elif mid == len(nums) - 1:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]
            elif nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            else:
                if mid % 2 == 1:
                    if nums[mid] == nums[mid - 1]:
                        i = mid + 1
                    else:
                        j = mid - 1
                else:
                    if nums[mid] == nums[mid + 1]:
                        i = mid + 1
                    else:
                        j = mid - 1
        return -1