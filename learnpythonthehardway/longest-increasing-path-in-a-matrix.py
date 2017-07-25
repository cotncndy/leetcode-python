# Time:  O(m * n)
# Space: O(m * n)

# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up
# or down. You may NOT move diagonally or move outside of the boundary
# (i.e. wrap-around is not allowed).
#
# Example 1:
#
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].
#
# Example 2:
#
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# DFS + Memorization solution.
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        def helper(matrix, dis, i, j):
            if dis[i][j]:
                return dis[i][j]
            dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            max_dist = 1
            for x, y in dir:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and \
                                matrix[i][j] > matrix[new_i][new_j]:
                    max_dist = max(max_dist, 1 + helper(matrix, dis, new_i, new_j))

            matrix[i][j] = max_dist
            return matrix[i][j]

        m, n = len(matrix), len(matrix[0])
        dis = [[0 for _ in xrange(n)] for _ in xrange(m)]

        res = 0
        for i in xrange(m):
            for j in xrange(n):
                res = max(res, helper(matrix, dis, i, j))

        return res
