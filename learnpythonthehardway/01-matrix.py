# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] > 0:
                    continue
                visited = [[False] * n for _ in xrange(m)]
                self.dfs(matrix, visited, 0, i, j)

        return matrix

    def dfs(self, matrix, visited, step, x, y):
        if visited[x][y]:
            return
        if matrix[x][y]:
            matrix[x][y] = min(matrix[x][y], step)
        visited[x][y] = True
        self.dfs(matrix, visited, step + 1, x + 1, y)
        self.dfs(matrix, visited, step + 1, x - 1, y)
        self.dfs(matrix, visited, step + 1, x, y + 1)
        self.dfs(matrix, visited, step + 1, x, y - 1)
