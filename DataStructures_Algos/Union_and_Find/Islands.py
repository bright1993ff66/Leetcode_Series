from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.
        :param grid:
        :return:
        """
        pass


if __name__ == '__main__':
    check_solution = Solution()
    result = check_solution.numIslands(grid=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
    print(result)
