# Time:  O(min(m, n)^2 * max(m, n) * log(max(m, n)))
# Space: O(max(m, n))

# Given a non-empty 2D matrix matrix and an integer k,
# find the max sum of a rectangle in the matrix such that its sum is no larger than k.
#
# Example:
# Given matrix = [
#   [1,  0, 1],
#   [0, -2, 3]
# ]
# k = 2
# The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]]
# is 2 and 2 is the max number no larger than k (k = 2).
#
# Note:
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?

# Time:  O(min(m, n)^2 * max(m, n)^2)
# Space: O(max(m, n))

# Given a non-empty 2D matrix matrix and an integer k,
# find the max sum of a rectangle in the matrix such that its sum is no larger than k.
#
# Example:
# Given matrix = [
#   [1,  0, 1],
#   [0, -2, 3]
# ]
# k = 2
# The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]]
# is 2 and 2 is the max number no larger than k (k = 2).
#
# Note:
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?

# Time:  O(min(m, n)^2 * max(m, n)^2)
# Space: O(max(m, n))
from bisect import bisect_left, insort


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # todo

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col, res = len(matrix), len(matrix[0]), float('-inf')
        dp = [[0] * col for _ in xrange(row)]
        for i in xrange(row):
            for j in xrange(col):
                t = matrix[i][j]
                if i == 0 and j > 0:
                    t += dp[i][j - 1]
                elif j == 0 and i > 0:
                    t += dp[i - 1][j]
                elif i > 0 and j > 0:
                    t += dp[i - 1][j - 1]
                dp[i][j] = t

                for r in xrange(0, i + 1):
                    for s in xrange(0, j + 1):
                        t = dp[i][j]  # bugfixed
                        if r > 0:
                            t -= dp[r - 1][j]
                            if s == 0:
                                if t <= k:
                                    res = max(res, t)
                        if s > 0:
                            t -= dp[i][s - 1]
                            if j == 0:
                                if t <= k:
                                    res = max(res, t)
                        if r > 0 and s > 0:
                            t += dp[r - 1][s - 1]
                            if t <= k:
                                res = max(res, t)
                        else:
                            if t <= k:
                                res = max(res, t)
        return res

    def maxSumSubmatrix2(self, matrix, k):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col, res = len(matrix), len(matrix[0]), float('-inf')
        dp = [[0] * col for _ in xrange(row)]
        for i in xrange(row):
            for j in xrange(col):
                t = matrix[i][j]
                if j > 0:
                    t += dp[i][j - 1]
                if i > 0:
                    t += dp[i - 1][j]
                if i > 0 and j > 0:
                    t -= dp[i - 1][j - 1]

                dp[i][j] = t

                for r in xrange(0, i + 1):
                    for s in xrange(0, j + 1):
                        t = dp[i][j]
                        if r > 0:
                            t -= dp[r - 1][j]
                        if s > 0:
                            t -= dp[i][s - 1]
                        if s > 0 and r > 0:
                            t += dp[r - 1][s - 1]

                        if t <= k:
                            res = max(res, t)
        return res


if __name__ == '__main__':
    print Solution().maxSumSubmatrix2([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 9)
