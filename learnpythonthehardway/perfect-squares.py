# Time:  O(n * sqrt(n))
# Space: O(n)
#
# Given a positive integer n, find the least number of perfect
# square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
# given n = 13, return 2 because 13 = 4 + 9.
#

class Solution(object):
    _num = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * n
        for i in xrange(n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
                j += 1

        return dp[n]
