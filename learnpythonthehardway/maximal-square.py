# Time:  O(n^2)
# Space: O(n)
#
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing all 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.
#

# DP with sliding window.
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in xrange(n)] for i in xrange(m)]
        max_size = 0

        for j in xrange(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in xrange(1, m):
            if matrix[i][0] == '1':
                size[i][0] = 1
            max_size = max(max_size, size[i][0])  # bugfixed

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    size[i][j] = min(size[i - 1][j], size[i][j - 1], size[i - 1][j - 1]) + 1
                    max_size = max(max_size, size[i][j])

        return max_size * max_size
