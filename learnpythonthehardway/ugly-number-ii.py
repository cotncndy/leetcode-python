# Time:  O(n)
# Space: O(1)
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors
# only include 2, 3, 5. For example,
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the
# first 10 ugly numbers.
#
# Note that 1 is typically treated as an ugly number.
#
# Hint:
#
# The naive approach is to call isUgly for every number
# until you reach the nth one. Most numbers are not ugly.
# Try to focus your effort on generating only the ugly ones.
#

import heapq


class Solution:
    ugly = sorted(2 ** a * 3 ** b * 5 ** c for a in xrange(32) for b in xrange(20) for c in xrange(14))

    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        return self.ugly[n - 1]
