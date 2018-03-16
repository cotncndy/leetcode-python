# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another if and only if one island
# can be translated (and not rotated or reflected) to equal the other.
#
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.
import collections


class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, pSet = len(grid), len(grid[0]), set()
        visited = [[False] * n for _ in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    li = []
                    self.dfs(grid, i, j, li, visited, i, j)
                    res = ""
                    for k in sorted(li):
                        res += str(k)
                    pSet.add(res)

        return len(pSet)

    def dfs(self, grid, x, y, li, visited, i, j):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] == 0:
            return
        li.append(((x - i) * len(grid[0]) + (y - j)) * (x - i))
        visited[x][y] = True
        self.dfs(grid, x - 1, y, li, visited, i, j)
        self.dfs(grid, x, y + 1, li, visited, i, j)
        self.dfs(grid, x + 1, y, li, visited, i, j)
        self.dfs(grid, x, y - 1, li, visited, i, j)

    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, pSet = len(grid), len(grid[0]), set()
        visited = [[False] * n for _ in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    li = []
                    self.dfs2(grid, i, j, li, visited, i, j)
                    res = ''.join(li)
                    pSet.add(res)

        return len(pSet)

    def dfs2(self, grid, x, y, li, visited, i, j):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] == 0:
            return
        li.append(str(x - i) + str(y - j))
        visited[x][y] = True
        self.dfs2(grid, x - 1, y, li, visited, i, j)
        self.dfs2(grid, x, y + 1, li, visited, i, j)
        self.dfs2(grid, x + 1, y, li, visited, i, j)
        self.dfs2(grid, x, y - 1, li, visited, i, j)
if __name__ == '__main__':
    print Solution().numDistinctIslands2([[1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 0, 1]])
    print Solution().numDistinctIslands([[1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 0, 1]])
