from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i_row = 0
        j_row = len(matrix) - 1
        while (i_row <= j_row):
            mid_row = i_row + (int)((j_row - i_row) / 2)
            if len(matrix[mid_row]) == 0:
                return False
            if matrix[mid_row][0] <= target and target <= matrix[mid_row][-1]:
                return self.searchArray(matrix[mid_row], target)
            elif target < matrix[mid_row][0]:
                j_row = mid_row - 1
            else:
                i_row = mid_row + 1
        return False

    def searchArray(self, arr: List[int], target: int) -> bool:
        i = 0
        j = len(arr) - 1
        while (i <= j):
            mid = i + (int)((j - i) / 2)
            if arr[mid] == target:
                return True
            elif target < arr[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return False
