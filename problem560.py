from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = defaultdict(lambda: 0)
        m[0] = 1
        res = 0
        sum = 0
        for num in nums:
            sum += num
            res += m[sum - k]
            m[sum] += 1
        return res
