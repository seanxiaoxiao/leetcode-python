from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for  j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.markIsland(grid, i, j)
                    res += 1
        return res

    def markIsland(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = '0'
            self.markIsland(grid, i - 1, j)
            self.markIsland(grid, i + 1, j)
            self.markIsland(grid, i, j - 1)
            self.markIsland(grid, i, j + 1)