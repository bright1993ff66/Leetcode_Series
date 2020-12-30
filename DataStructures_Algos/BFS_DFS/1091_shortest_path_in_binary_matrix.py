from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0: return -1
        ans, m, n = 0, len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1: return -1
        queue = [(0, 0)]
        while queue:
            tmp = []
            ans += 1
            for _ in range(len(queue)):
                x, y = queue.pop(-1)
                if (x, y) == (m-1, n-1): return ans
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1):
                    xx, yy = x+dx, y+dy
                    if 0 <= xx < m and 0 <= yy < n and not grid[xx][yy]:
                        grid[xx][yy] = 1
                        tmp.append((xx, yy))
            queue = tmp
        return -1