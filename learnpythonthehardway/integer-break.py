# Time:  O(logn), pow is O(logn).
# Space: O(1)

# Given a positive integer n, break it into the sum of
# at least two positive integers and maximize the product
# of those integers. Return the maximum product you can get.
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10,
# return 36 (10 = 3 + 3 + 4).
#
# Note: you may assume that n is not less than 2.
#
# Hint:
#
# There is a simple O(n) solution to this problem.
# You may check the breaking results of n ranging from 7 to 10
# to discover the regularities.

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3:
            return n - 1
        res = 1
        while n > 4:
            res *= 3
            n -= 3

        return res * n
