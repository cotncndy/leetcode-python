# Time:  O(m * n)
# Space: O(m * n)

# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and
# top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right)
# from a cell to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#       ~  1   2   2   3  (5) *
#       ~  3   2   3  (4) (4) *
#       ~  2   4  (5)  3   1  *
#       ~ (6) (7)  1   4   5  *
#       ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        PACIFIC, ATLANTIC = 1, 2

        def dfs(matrix, i, j, prev_height, ocean, visited, res):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and \
                            matrix[i][j] >= prev_height and \
                            (visited[i][j] | ocean) != ocean:  # notice
                visited[i][
                    j] |= ocean  # review, by using bitwise, we don't need two visited set to record, whereby avoiding searching for intersect.
                if visited[i][j] == (PACIFIC | ATLANTIC):
                    res.append((i, j))

                dfs(matrix, i + 1, j, matrix[i][j], ocean, visited, res)
                dfs(matrix, i - 1, j, matrix[i][j], ocean, visited, res)
                dfs(matrix, i, j + 1, matrix[i][j], ocean, visited, res)
                dfs(matrix, i, j - 1, matrix[i][j], ocean, visited, res)

        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        visited, res = [[0 for _ in xrange(n)] for _ in xrange(m)], []
        for i in xrange(m):
            dfs(matrix, i, 0, float('-inf'), PACIFIC, visited, res)
            dfs(matrix, i, n - 1, float('-inf'), ATLANTIC, visited, res)

        for j in xrange(n):
            dfs(matrix, 0, j, float('-inf'), PACIFIC, visited, res)
            dfs(matrix, m - 1, j, float('-inf'), ATLANTIC, visited, res)

        return res


if __name__ == '__main__':
    matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7.1, 4, 5], [5, 1, 1, 2, 4]]
    print Solution().pacificAtlantic(matrix)
