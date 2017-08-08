# Time:  O(m * n)
# Space: O(m * n)

import copy
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not len(grid) or not len(grid[0]):
            return 0
        m, n, res = len(grid), len(grid[0]), 0
        up = [[0] * n for _ in xrange(m)]
        # knowledge 2 -ways about 2 -ways about how to copy a 2-d list
        down, left, right = [x[:] for x in up], [x[:] for x in up], copy.deepcopy(up)

        for i in xrange(m):
            for j in xrange(n):
                t = 0 if j == 0 or grid[i][j - 1] == 'W' else left[i][j - 1]
                left[i][j] = t + 1 if grid[i][j] == 'E' else t

            for j in reversed(xrange(n)):
                t = 0 if j == n - 1 or grid[i][j + 1] == 'W' else right[i][j + 1]
                right[i][j] = t + 1 if grid[i][j] == 'E' else t

        for j in xrange(n):
            for i in xrange(m):
                t = 0 if i == 0 or grid[i - 1][j] == 'W' else up[i - 1][j]
                up[i][j] = t + 1 if grid[i][j] == 'E' else t

            for i in reversed(xrange(m)):
                t = 0 if i == m - 1 or grid[i + 1][j] == 'W' else down[i + 1][j]
                down[i][j] = t + 1 if grid[i][j] == 'E' else t

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '0':
                    res = max(res, up[i][j] + down[i][j] + left[i][j] + right[i][j])

        return res


if __name__ == '__main__':
    print Solution().maxKilledEnemies([['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0']])
