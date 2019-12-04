class Solution:
    def minTotalDistance(self, grid) -> int:
        h = []
        v = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    h.append(i)
                    v.append(j)

        h.sort()
        v.sort()
        dist = 0
        len_h = len(h)
        len_v = len(v)
        for i in range(len_h / 2):
            dist += h[len_h - 1 -i] - h[i]
        for i in range(len_v / 2):
            dist += v[len_v - 1 - i] - v[i]
        return dist
