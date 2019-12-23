from typing import List
import functools

def interval_compare(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    else:
        return y[1] - x[1]

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=functools.cmp_to_key(interval_compare), reverse=False)
        i = 0
        while i < len(intervals) - 1:
            interval_prev = intervals[i]
            merged = False
            for j in range(i + 1, len(intervals)):
                interval_curr = intervals[j]
                if self.isIntervalContain(interval_prev, interval_curr):
                    del intervals[j]
                    merged = True
                    break
            if not merged:
                i += 1
        return len(intervals)

    def isIntervalContain(self, interval1, interval2):
        return interval1[0] <= interval2[0] and interval1[1] >= interval2[1]

s = Solution()
print(s.removeCoveredIntervals([[1,4],[3,6],[2,8]]))