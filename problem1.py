class Solution:
    def twoSum(self, nums, target):
        num_index_map = {}
        for i, num in enumerate(nums):
            num_index_map[num] = i
        for i, num in enumerate(nums):
            if target - num in num_index_map and i != num_index_map[target - num]:
                return [i, num_index_map[target - num]]
        return []
