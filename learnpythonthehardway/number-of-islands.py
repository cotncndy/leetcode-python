# Time:  O(m * n)
# Space: O(m * n)
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        used = [[False for j in xrange(col)] for i in xrange(row)]

        cnt = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1' and not used[i][j]:
                    self.dfs(grid, used, i, j, row, col)
                    cnt += 1
        return cnt

    def dfs(self, grid, used, x, y, row, col):  # this is more convinient and undstandable than union find
        if grid[x][y] == '0' or used[x][y]:
            return
        used[x][y] = True
        if x != 0:
            self.dfs(grid, used, x - 1, y, row, col)
        if x != row - 1:
            self.dfs(grid, used, x + 1, y, row, col)
        if y != 0:
            self.dfs(grid, used, x, y - 1, row, col)
        if y != col - 1:
            self.dfs(grid, used, x, y + 1, row, col)
