# Time:  O(m * n)
# Space: O(n)
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        size = len(triangle)
        dp = list(triangle[-1])

        for i in reversed(xrange(size - 1)):
            for j in xrange(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]
